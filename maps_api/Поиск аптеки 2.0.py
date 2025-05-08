import requests
import sys
import math
import pygame
import os


def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000  # 111 километров в метрах
    a_lon, a_lat = a
    b_lon, b_lat = b

    # Берем среднюю по широте точку и считаем коэффициент для нее.
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    # Вычисляем смещения в метрах по вертикали и горизонтали.
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    # Вычисляем расстояние между точками.
    distance = math.sqrt(dx * dx + dy * dy)

    return distance


search_api_server = "https://search-maps.yandex.ru/v1/"
search_api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_api_key = "cf79098a-155e-47b7-9b49-b55b4461472d"

static_api_server = "https://static-maps.yandex.ru/v1?"
static_api_key = "318965a9-b51c-41fb-a672-2acad73bc050"

search_params = {
    "apikey": search_api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": "",
    "type": "biz"
}

print("Введите адрес: ", end='')
address = input()

geocoder_params = {
    "apikey": geocoder_api_key,
    "geocode": address,
    "format": "json"
}

static_api_params = {
    "apikey": static_api_key,
    "pt": ""
}

response = requests.get(geocoder_api_server, params=geocoder_params).json()

if not response["response"]["GeoObjectCollection"]["featureMember"]:
    print("Объект не найден")
    sys.exit(1)

ll = ','.join(response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split())
search_params["ll"] = ll

response = requests.get(search_api_server, params=search_params).json()

if not response["features"]:
    print("Рядом нет аптек")
    sys.exit(1)

arr = []
for el in response["features"]:
    cur_ll = el["geometry"]["coordinates"]
    d = lonlat_distance(list(map(float, ll.split(','))), cur_ll)
    cur_address = el["properties"]["CompanyMetaData"]["address"]
    hours = el["properties"]["CompanyMetaData"]["Hours"]["text"]
    name = el["properties"]["name"]
    arr.append((d, cur_ll, cur_address, hours, name))

arr = sorted(arr, key=lambda x: x[0])
info_obj = {
    "расстояние": arr[0][0],
    "название": arr[0][4],
    "адрес": arr[0][2],
    "режим работы": arr[0][3]
}
print(info_obj)
points = [ll, ','.join(list(map(str, arr[0][1])))]
for i in range(len(points)):
    points[i] = ','.join(points[i].split(',') + ["pm2dgl"])

static_api_params["pt"] = "~".join(points)

response = requests.get(static_api_server, params=static_api_params)
if not response:
    print("Ошибка")
    sys.exit(1)

with open("map.png", "wb") as f:
    f.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load("map.png"), (0, 0))
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove("map.png")

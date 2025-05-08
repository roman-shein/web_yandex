import requests
import sys
import math
import pygame
import os


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
points = []
for el in response["features"]:
    point = list(map(str, el["geometry"]["coordinates"]))
    if "Hours" in el["properties"]["CompanyMetaData"].keys():
        if "TwentyFourHours" in el["properties"]["CompanyMetaData"]["Hours"]["Availabilities"][0]:
            point.append("pm2gnl")
        else:
            point.append("pm2bll")
    else:
        point.append("pm2grl")
    # print(el["properties"]["CompanyMetaData"].keys())
    points.append(','.join(point))


static_api_params["pt"] = "~".join(points)

response = requests.get(static_api_server, params=static_api_params)
if not response:
    print(response.content)
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

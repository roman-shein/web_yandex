import sys

import requests
import math


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


print("Введите адрес объекта: ", end='')
address = input()

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

params = {
    "apikey": "cf79098a-155e-47b7-9b49-b55b4461472d",
    "geocode": address,
    "format": "json"
}

response = requests.get(geocoder_api_server, params=params).json()
if not response["response"]["GeoObjectCollection"]["featureMember"]:
    print("Объект не найден")
    sys.exit(1)
ll = ','.join(response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split())
ll_for_math = list(map(float, ll.split(',')))
params["geocode"] = ll
params["kind"] = "metro"
# print(response, file=open("data.json", 'w', encoding="utf8"))
response = requests.get(geocoder_api_server, params=params).json()
if not response["response"]["GeoObjectCollection"]["featureMember"]:
    print("Рядом с этим адресом нет станций метро")
    sys.exit(1)

# print(response, file=open("data.json", 'w', encoding="utf8"))
objects = response["response"]["GeoObjectCollection"]["featureMember"]
arr = []
for el in objects:
    ll_obj = list(map(float, el["GeoObject"]["Point"]["pos"].split()))
    distance = lonlat_distance(ll_for_math, ll_obj)
    arr.append((el["GeoObject"]["name"], distance))

print(sorted(arr, key=lambda x: x[1])[0][0])

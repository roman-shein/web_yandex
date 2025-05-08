import sys
import math

import requests


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


print("Введите адрес дома: ", end='')
home = input()
print("Введите адрес школы: ", end='')
school = input()
s = """
мурманск бочкова 5
мурманск баумана 11
"""
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

params = {
    "apikey": "cf79098a-155e-47b7-9b49-b55b4461472d",
    "geocode": "",
    "format": "json"
}

arr = []
for el in [home, school]:
    params["geocode"] = el
    response = requests.get(geocoder_api_server, params=params).json()
    if not response["response"]["GeoObjectCollection"]["featureMember"]:
        print("Объект не найден")
        sys.exit(1)
    ll = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split()
    ll = list(map(float, ll))
    arr.append(ll)

print(int(lonlat_distance(arr[0], arr[1])), "метры")


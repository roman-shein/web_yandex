import sys
import pygame
import os
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


server_address = "https://static-maps.yandex.ru/v1?"

points = ["37.619881,55.753673",
          "37.619178,55.755416",
          "37.616152,55.754783",
          "37.609428,55.751347",
          "37.610179,55.749619",
          "37.612583,55.748931",
          "37.613695,55.748118"]
params = {
    "apikey": "318965a9-b51c-41fb-a672-2acad73bc050",
    "pl": ','.join(points)
}

distance = 0
for i in range(len(points) - 1):
    ll_1 = list(map(float, points[i].split(',')[::-1]))
    ll_2 = list(map(float, points[i + 1].split(',')[::-1]))
    distance += lonlat_distance(ll_1, ll_2)
print(int(distance), "метров")
cur_dist = 0
for i in range(len(points) - 1):
    ll_1 = list(map(float, points[i].split(',')[::-1]))
    ll_2 = list(map(float, points[i + 1].split(',')[::-1]))
    d = lonlat_distance(ll_1, ll_2)
    if cur_dist + d > distance / 2:
        k = (distance / 2 - cur_dist) / d
        lon = str(ll_1[0] + (ll_2[0] - ll_1[0]) * k)
        lat = str(ll_1[1] + (ll_2[1] - ll_1[1]) * k)
        params["pt"] = ','.join([lat, lon, "pm2dgl"])
        break
    cur_dist += d

request = requests.get(server_address, params=params)
if not request:
    sys.exit(1)

with open("map.png", 'wb') as f:
    f.write(request.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load("map.png"), (0, 0))
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove("map.png")

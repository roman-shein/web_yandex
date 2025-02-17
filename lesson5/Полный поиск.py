import sys
from lib_search import find_ll_spn, make_map
import pygame
import os

toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
    "geocode": toponym_to_find,
    "format": "json"}

ll, spn = find_ll_spn(geocoder_api_server, geocoder_params)
if not (ll and spn):
    print(f"{toponym_to_find} - not found")
    sys.exit(0)
server_address_maps = "https://static-maps.yandex.ru/v1?"

map_params = {
    "ll": ll,
    "spn": spn,
    "apikey": "ef67d706-4387-4517-8b08-50f4c0929dd7",
    "pt": "{0},pm2dgl".format(ll)
}

name_maps = make_map(server_address_maps, map_params)
if name_maps:
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(name_maps), (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

    # Удаляем за собой файл с изображением.
    # os.remove(name_maps)

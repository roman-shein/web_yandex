import sys
import pygame
import os

import requests

server_address = "https://static-maps.yandex.ru/v1?"

points = ['29.914162,59.894599',
          '30.218152,59.921265',
          '30.263049,59.916782',
          '30.275994,59.931487',
          '30.312354,59.941370']

params = {
    "apikey": "318965a9-b51c-41fb-a672-2acad73bc050",
    "pl": ','.join(points)
}

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

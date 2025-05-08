import sys
import pygame
import os

import requests

server_address = "https://static-maps.yandex.ru/v1?"

points = ["37.440365,55.817827,pm2dgl",
          "37.559340,55.790980,pm2dgl",
          "37.553728,55.715742,pm2dgl"]
params = {
    "apikey": "318965a9-b51c-41fb-a672-2acad73bc050",
    "spn": "0.09,0.09",
    "ll": "37.617698,55.755864",
    "pt": '~'.join(points)
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

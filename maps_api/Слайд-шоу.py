import os

import requests
import pygame

server_address = "https://static-maps.yandex.ru/v1?"
objects = ["-89.399493,35.060156",
           "60.097095,53.297914",
           "123.943641,53.987177",
           "27.987893,-26.123753",
           "12.455707,41.902185"]

params = {
    "apikey": "318965a9-b51c-41fb-a672-2acad73bc050",
    "spn": "0.01,0.01",
    "ll": ""
}


def search_img(n):
    global screen
    coord = objects[n]
    if n == 3:
        params["spn"] = "0.2,0.2"
    else:
        params["spn"] = "0.01,0.01"
    params["ll"] = coord
    response = requests.get(server_address, params=params)
    if not response:
        return
    with open("map.png", "wb") as f:
        f.write(response.content)
    screen.blit(pygame.image.load("map.png"), (0, 0))
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((600, 450))
c = 0
search_img(c)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            c = (c + 1) % len(objects)
            search_img(c)

os.remove("map.png")

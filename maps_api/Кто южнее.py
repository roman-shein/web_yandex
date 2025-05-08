import requests

server_address = "http://geocode-maps.yandex.ru/1.x/?"

params = {
    "apikey": "cf79098a-155e-47b7-9b49-b55b4461472d",
    "geocode": "",
    "format": "json"
}

cities = input().split(', ')
d = []
for city in cities:
    params["geocode"] = city
    response = requests.get(server_address, params).json()
    if not response:
        continue
    coords = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split()[1]
    d.append((city, float(coords)))

print(sorted(d, key=lambda x: x[1])[0][0])





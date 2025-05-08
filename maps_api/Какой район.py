import requests
import sys

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

params["geocode"] = ll
params["kind"] = "district"
response = requests.get(geocoder_api_server, params=params).json()
if not response["response"]["GeoObjectCollection"]["featureMember"]:
    print("Объект не найден")
    sys.exit(1)
print(response, file=open("data.json", 'w', encoding="utf8"))
print(response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["name"])

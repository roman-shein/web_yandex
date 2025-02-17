import requests


def find_ll_spn(geocoder_api_server, geocoder_params):
    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        return None, None

    # # Преобразуем ответ в json-объект
    json_response = response.json()

    av_search = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']

    lowerCorner = av_search['boundedBy']['Envelope']['lowerCorner']
    upperCorner = av_search['boundedBy']['Envelope']['upperCorner']

    lon1, lat1 = map(float, lowerCorner.split())
    lon2, lat2 = map(float, upperCorner.split())

    ll = ','.join(av_search["Point"]["pos"].split())

    spn = str(abs(lon1 - lon2)), str(abs(lat1 - lat2))
    spn = ",".join(spn)
    return ll, spn

def make_map(server_address_maps, maps_params):
    response = requests.get(server_address_maps, maps_params)
    if not response:
        return None

    map_file = "map.png"

    with open(map_file, "wb") as file:
        file.write(response.content)

    return map_file

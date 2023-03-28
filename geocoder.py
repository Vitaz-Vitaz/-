import requests

def get_map_params(toponym_to_find):
    g = "http://geocode-maps.yandex.ru/1.x/"
    gp = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get(g, params=gp)
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    lc, uc = toponym["boundedBy"]['Envelope']['lowerCorner'], toponym["boundedBy"]['Envelope']['upperCorner']
    lc = list(map(float, lc.split()))
    uc = list(map(float, uc.split()))
    delta = abs(uc[0] - lc[0]), abs(uc[1] - lc[1])
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": f'{delta[0]},{delta[1]}',
        "l": "map"
    }
    return map_params

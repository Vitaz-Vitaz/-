import sys
from io import BytesIO
from geocoder_map_scaler import get_map_params
import requests
from PIL import Image

find = " ".join(sys.argv[1:])
map_api_server = "http://static-maps.yandex.ru/1.x/"
p = get_map_params(find)
p['pt'] = f'{p["ll"]},pm2rdm'
response = requests.get(map_api_server, params=p)

Image.open(BytesIO(
    response.content)).show()

import json
import requests
from pprint import pprint

api_url_base='https://www.dolarsi.com/api/api.php?type=valoresprincipales'


def get_account_info():
    api_url='{0}account'.format(api_url_base)
    response = requests.get(api_url_base)
    if response.status_code == 200:
        return response.json()
    else:
        return None

respuesta = get_account_info()

for dolar in respuesta:
    print(dolar['casa']['nombre'])   
    print(dolar['casa']['venta'])
    print('****')



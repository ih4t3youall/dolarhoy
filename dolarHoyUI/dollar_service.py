import json
import requests
from dollar import Dollar
from datetime import date


api_url_base='https://www.dolarsi.com/api/api.php?type=valoresprincipales'

def get_account_info():
    api_url='{0}account'.format(api_url_base)
    response = requests.get(api_url_base)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_dollars():
    response = get_account_info()
    name_oficial = response[0]['casa']['nombre']
    price_oficial = response[0]['casa']['venta']
    name_blue = response[1]['casa']['nombre']
    price_blue = response[1]['casa']['venta']
    dollar_oficial = Dollar(name_oficial,price_oficial,date.today())
    dollar_blue = Dollar(name_blue,price_blue,date.today())
    dollars ={}
    dollars['blue'] = dollar_blue
    dollars['oficial'] = dollar_oficial
    return dollars


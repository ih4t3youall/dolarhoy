import json
import requests
from pprint import pprint
from dollar import Dollar
from calculadora import Calculadora

api_url_base='https://www.dolarsi.com/api/api.php?type=valoresprincipales'


def get_account_info():
    api_url='{0}account'.format(api_url_base)
    response = requests.get(api_url_base)
    if response.status_code == 200:
        return response.json()
    else:
        return None

respuesta = get_account_info()

def all_dollar_prices(respuesta):
    for dolar in respuesta:
        print(dolar['casa']['nombre'])   
        print(dolar['casa']['venta'])
        print('****')

def dolar_blue(respuesta):
    precio =respuesta[1]['casa']['venta'];
    nombre =respuesta[1]['casa']['nombre'];
    dolar_blue = Dollar(nombre,precio)
    return dolar_blue

def dolar_oficial(respuesta):
    precio =respuesta[0]['casa']['venta'];
    nombre =respuesta[0]['casa']['nombre'];
    dolar_oficial = Dollar(nombre,precio)
    return dolar_oficial


dolar_blue = dolar_blue(respuesta)
dolar_oficial= dolar_oficial(respuesta)
dolar_blue.imprimir_dolar()
dolar_oficial.imprimir_dolar()

calculadora = Calculadora(dolar_blue,dolar_oficial)
print('ingrese cantidad de dolar oficial')
dolar_billete = float(input())
calculadora.calcular(dolar_billete)


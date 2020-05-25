import json
import requests
from pprint import pprint
from dollar import Dollar
from calculadora import Calculadora
from saveDollar import Save_dollar
from datetime import date

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
    price =respuesta[1]['casa']['venta'];
    name =respuesta[1]['casa']['nombre'];
    dolar_blue = Dollar(name,price,date.today())
    return dolar_blue

def dolar_oficial(respuesta):
    price =respuesta[0]['casa']['venta'];
    name =respuesta[0]['casa']['nombre'];
    dolar_oficial = Dollar(name,price,date.today())
    return dolar_oficial


dolar_blue = dolar_blue(respuesta)
dolar_oficial= dolar_oficial(respuesta)
dolar_blue.imprimir_dolar()
dolar_oficial.imprimir_dolar()

calculadora = Calculadora(dolar_blue,dolar_oficial)
print('ingrese cantidad de dolar oficial')
#dolar_billete = float(input())
dolar_billete = float(1000)
calculadora.calcular(dolar_billete)

flag = True
while flag:
    print('1: grabo con append ')
    print('2: leo y me traigo la lista')
    print('3: agrego dolares de prueba')
    desicion =int(input())
    dolar_saver = Save_dollar()
    
    
    
    
    if desicion == 1:
        dolar_saver.append_dollar(dolar_blue)
    if desicion == 2:
        lista_dollar = dolar_saver.read_all()
        for dollar in lista_dollar:
            print(dollar.price)
    if desicion == 3:
        dollar1 = Dollar('dollar1','300',date.today())
        dollar2 = Dollar('dollar2','400',date.today())
        dolar_saver.append_dollar(dollar1)
        dolar_saver.append_dollar(dollar2)
    print('desea realizar otra operacion')
    print('1 si')
    print('2 no')
    operacion = input()
    if operacion == '2':
        flag = False

import json
import requests
from pprint import pprint
from dollar import Dollar
from calculadora import Calculadora
from saveDollar import Save_dollar
from datetime import date
import time
from os import system, name
from dollar_service import get_dollars
import sys, traceback

dollars = get_dollars()
dolar_blue = dollars['blue']
dolar_oficial= dollars['oficial']

def calcular_compra_dolar():
    calculadora = Calculadora(dolar_blue,dolar_oficial)
    print('ingrese cantidad de dolar oficial')
    dolar_billete = float(input())
    calculadora.calcular(dolar_billete)

flag = True
desicion = 99
while flag:
    dolar_blue.pretty_print()
    dolar_oficial.pretty_print()
    _ = system('clear')
    print('1: imprimir dolar historico')
    print('2: salvar dolar hoy')
    print('3: calcular dolar oficial')
    print('9: agrego dolares de prueba')
    print('0: salir')
    desicion =int(input())
    dolar_saver = Save_dollar()
    
    if desicion == 1:
        lista_dollar = dolar_saver.read_all()
        for dollar in lista_dollar:
            dollar.imprimir_dolar()
    if desicion == 2:
        allhistoric = dolar_saver.read_all()
        try:
            last_dollar_saved= allhistoric[len(allhistoric)-1]
            if last_dollar_saved is not None:
                if dolar_blue.date > last_dollar_saved.date:
                    dolar_saver.append_dollar(dolar_blue)
                else:
                    #equals or less
                    if last_dollar_saved.price != dolar_blue.price:
                        print('sobre escribo el ultimo registro')
                        dolar_saver.update_last_one(dolar_blue)
                    else:
                        print('same price not update')
            else:
                dolar_saver.append_dollar(dolar_blue)
        except Exception:
           # traceback.print_exc(file=sys.stdout) 
            print('exception')
            dolar_saver.save_dollar(dolar_blue)
    if desicion == 3:
        calcular_compra_dolar()
    if desicion == 9:
        dollar1 = Dollar('dollar1','300',date.today())
        dollar2 = Dollar('dollar2','400',date.today())
        dolar_saver.append_dollar(dollar1)
        dolar_saver.append_dollar(dollar2)
    if desicion == 0:
        break
    input()

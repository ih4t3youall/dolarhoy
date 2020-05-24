from dollar import Dollar

class Calculadora:

    def __init__(self,dolar_blue:Dollar,dolar_oficial:Dollar):
        self.dolar_blue = dolar_blue
        self.dolar_oficial = dolar_oficial

    def calcular(self,dolar_billete):
        pesos_oficial = dolar_billete * self.dolar_oficial.precio
        print('cantidad de dolar blue: ')
        print(float(pesos_oficial)/self.dolar_blue.precio)

        

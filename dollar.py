from datetime import date
class Dollar:
    def __init__(self,name,price,date):
       self.price = float(price.replace(',','.'))
       self.name = name
       self.date = date

    def imprimir_dolar(self):
        print(self.name)
        print(self.price)
        print(self.date)
    def pretty_print(self):
        print(self.name)
        print(self.price)

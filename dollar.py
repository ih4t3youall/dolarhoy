class Dollar:
    def __init__(self,nombre,precio):
       self.precio = float(precio.replace(',','.'))
       self.nombre = nombre

    def imprimir_dolar(self):
        print(self.nombre)
        print(self.precio)

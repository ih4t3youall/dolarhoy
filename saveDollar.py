try:
       import cPickle as pickle
except:
       import pickle

from dollar import Dollar

class Save_dollar:

    path='/home/juan.martin.lequerica/env/dolarhoy.txt'

    def save_dollar(self,dollar):
        file = open(self.path,'wb')
        pickle.dump(dollar, file, pickle.HIGHEST_PROTOCOL)
    def read_dollar(self):
        file = open(self.path,'rb')
        dollar:Dollar = pickle.load(file)
        print('imprimo dolar')
        dollar.imprimir_dolar()
    def append_dollar(self,dollar):
        file = open(self.path,mode='a+b')
        pickle.dump(dollar,file)

    def read_all(self):
        file = open(self.path,'rb')
        listaDollar =[]
        while True:
            try:
                dollars:Dollar= pickle.load(file)
                listaDollar.append(dollars)
            except EOFError:
                print('devolviendo listadollar')
                return listaDollar
                break

    def read_two(self):
        file = open(self.path,'rb')
        while True:
            try:
                dollars:Dollar= pickle.load(file)
                dollars.imprimir_dolar()
            except EOFError:
                break
        
        
        



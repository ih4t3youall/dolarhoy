try:
       import cPickle as pickle
except:
       import pickle

import datetime
from dollar import Dollar
import os


class Save_dollar:

    path='/home/juan.martin.lequerica/env/dolarhoy.txt'

    def save_dollar(self,dollar):
        file = open(self.path,'wb')
        pickle.dump(dollar, file, pickle.HIGHEST_PROTOCOL)
    def append_dollar(self,dollar):
        if not os.path.exists(self.path):
            with open(self.path, 'w'): pass
        file = open(self.path,mode='a+b')
        pickle.dump(dollar,file)
        file.close()
    def read_all(self):
        try:
            file = open(self.path,'rb')
        except FileNotFoundError:
            open(self.path, 'w')
            return None
        listaDollar =[]
        while True:
            try:
                dollars:Dollar= pickle.load(file)
                listaDollar.append(dollars)
            except EOFError:
                return listaDollar
    def update_last_one(self,dolar_blue):
        lista = self.read_all()
        old_dollar = lista[len(lista)-1]
        old_dollar.price = dolar_blue.price
        self.update_file(lista)
    def update_file(self,dollar_list):
        open(self.path, "w").close()
        file = open(self.path, "wb")
        for dollar in dollar_list:
            pickle.dump(dollar,file)
        file.close() 

        
        



from calculadora import Calculadora
from tkinter import *
from tkinter import ttk, font
from saveDollar import Save_dollar
from dollar_service import get_dollars
import getpass
import datetime
from dollar import Dollar
import traceback

# La clase 'Aplicacion' ha crecido. En el ejemplo se incluyen
# nuevos widgets en el método constructor __init__(): Uno de
# ellos es el botón 'Info'  que cuando sea presionado llamará 
# al método 'verinfo' para mostrar información en el otro 
# widget, una caja de texto: un evento ejecuta una acción: 

class Aplicacion():
    def __init__(self):
        self.dollar_saver = Save_dollar()
        dollars= get_dollars()
        self.dolar_blue =dollars['blue']
        self.dolar_oficial = dollars['oficial']
        self.calculadora = Calculadora(self.dolar_blue,self.dolar_oficial)
        

        self.raiz = Tk()
        self.raiz.geometry('600x400')

        #defino la fuente
        fuente = font.Font(weight='bold')

        self.etiq1 = ttk.Label(self.raiz, text="Dolar Oficial:",
                               font=fuente)

        self.cantidad = StringVar()
        self.ctext1 = ttk.Entry(self.raiz,
                                textvariable=self.cantidad,
                                width=10)
        
        # Impide que los bordes puedan desplazarse para
        # ampliar o reducir el tamaño de la ventana 'self.raiz':
        
        self.raiz.resizable(width=False,height=False)
        self.raiz.title('Ver info')
        
        # Define el widget Text 'self.tinfo ' en el que se
        # pueden introducir varias líneas de texto:
        
        self.tinfo = Text(self.raiz, width=70, height=10)
        
        # Sitúa la caja de texto 'self.tinfo' en la parte
        # superior de la ventana 'self.raiz':
        
        self.tinfo.pack(side=TOP)
        self.ctext1.pack(side=TOP, fill=X, expand=False,
                        padx=5, pady=5)
        self.boton_cal_dollar = ttk.Button(self.raiz,text='calc Dollar',command=self.calc_dollar)
        self.boton_cal_dollar.pack(side=TOP)
        
        # Define el widget Button 'self.binfo' que llamará 
        # al metodo 'self.verinfo' cuando sea presionado
        
        self.bhistoric = ttk.Button(self.raiz, text='Historico', 
                                command=self.dol_historic)
        
        # Coloca el botón 'self.binfo' debajo y a la izquierda
        # del widget anterior
                                
        self.bhistoric.pack(side=LEFT)


        self.save_today_dollar = ttk.Button(self.raiz,text='save Dollar',command=self.save_dollar)
        self.save_today_dollar.pack(side=LEFT)
        #dolar ahora
        self.save_today_dollar = ttk.Button(self.raiz,text='Dollar now',command=self.dollar_now)
        self.save_today_dollar.pack(side=LEFT)
        #test
        self.save_today_dollar = ttk.Button(self.raiz,text='test',command=self.create_test)
        self.save_today_dollar.pack(side=LEFT)
        
        # Define el botón 'self.bsalir'. En este caso
        # cuando sea presionado, el método destruirá o
        # terminará la aplicación-ventana 'self.raíz' con 
        # 'self.raiz.destroy'
        
        self.bsalir = ttk.Button(self.raiz, text='Salir', 
                                 command=self.raiz.destroy)
                                 
        # Coloca el botón 'self.bsalir' a la derecha del 
        # objeto anterior.
                                 
        self.bsalir.pack(side=LEFT)
        
        # El foco de la aplicación se sitúa en el botón
        # 'self.binfo' resaltando su borde. Si se presiona
        # la barra espaciadora el botón que tiene el foco
        # será pulsado. El foco puede cambiar de un widget
        # a otro con la tecla tabulador [tab]
        
        self.bhistoric.focus_set()
        self.raiz.mainloop()

    def fill_textbox(self,data):
        self.tinfo.delete(1.0,END)
        self.tinfo.insert(1.0, str(data))

    def calc_dollar(self):
        dolar_billete = self.ctext1.get()
        final = self.calculadora.calcular(float(dolar_billete))
        final = 'Pagas en blue \n'+str(final)
        self.fill_textbox(final)
    def dol_historic(self):
        lista_dollar = self.dollar_saver.read_all()
        text=''
        for dollar in lista_dollar:
            print('i was here too')
            text+=dollar.name + ': '+ str(dollar.price)+', fecha: '+ str(dollar.date)
            text+='\n'
        self.fill_textbox(text)
    def save_dollar(self):
        self.dollar_now()
        aDate = datetime.date(2020, 6, 30)
        self.dolar_blue = Dollar('dolar blue prueba','130.0',aDate)
        allhistoric = self.dollar_saver.read_all()
        try:
            last_dollar_saved= allhistoric[len(allhistoric)-1]
            if last_dollar_saved is not None:
                if self.dolar_blue.date > last_dollar_saved.date:
                    self.dollar_saver.append_dollar(self.dolar_blue)
                    self.fill_textbox('new dollar saved')
                else:
                    #equals or less
                    if last_dollar_saved.price != self.dolar_blue.price:
                        print('sobre escribo el ultimo registro')
                        self.fill_textbox('sobre escribo el ultimo registro')
                        self.dollar_saver.update_last_one(self.dolar_blue)
                    else:
                        print('same price not update')
                        self.fill_textbox('same price not update')
            else:
                self.dollar_saver.append_dollar(self.dolar_blue)
        except Exception:
            traceback.print_exc(file=sys.stdout) 
            print('exception')
            self.fill_textbox('not rebasing')
            self.dollar_saver.save_dollar(self.dolar_blue)

    def dollar_now(self):
        dollars = get_dollars()
        self.dolar_blue = dollars['blue']
        self.dolar_oficial = dollars['oficial']
        text='dolar now:\n'
        text=text+dollars['blue'].name+': '+str(dollars['blue'].price)+'\n'
        text=text+dollars['oficial'].name+': '+str(dollars['oficial'].price)
        self.fill_textbox(text)
    def create_test(self):
        print('i was here')
        aDate = datetime.date(2019, 6, 15)
        dolar1 = Dollar('dolar a','120.0',aDate)
        aDate2 = datetime.date(2019, 6, 16)
        dolar2 = Dollar('dolar b','122.0',aDate2)
        self.dollar_saver.append_dollar(dolar1)
        self.dollar_saver.append_dollar(dolar2)
        

    

def main():
    mi_app = Aplicacion()
    return 0


#__name__ devuelve el nobre del file si estoy en el ejecutor devuelve __main__
if __name__ == '__main__':
    main()

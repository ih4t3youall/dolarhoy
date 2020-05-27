from calculadora import Calculadora
from tkinter import *
from tkinter import ttk, font
from saveDollar import Save_dollar
from dollar_service import get_dollars
import getpass

# La clase 'Aplicacion' ha crecido. En el ejemplo se incluyen
# nuevos widgets en el método constructor __init__(): Uno de
# ellos es el botón 'Info'  que cuando sea presionado llamará 
# al método 'verinfo' para mostrar información en el otro 
# widget, una caja de texto: un evento ejecuta una acción: 

class Aplicacion():
    def __init__(self):
        self.dollar_saver = Save_dollar()
        dollars= get_dollars()
        self.calculadora = Calculadora(dollars['blue'],dollars['oficial'])
        
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
        self.fill_textbox(final)
    def dol_historic(self):
        lista_dollar = self.dollar_saver.read_all()
        text=''
        for dollar in lista_dollar:
            text+=dollar.name + ': '+ str(dollar.price)+', fecha: '+ str(dollar.date)
        self.fill_textbox(text)
    def save_dollar(self):
        save_dollar = 'salvando el dolar'
        self.fill_textbox(save_dollar)
    def dollar_now(self):
        dollars = get_dollars()
        text=dollars['blue'].name+': '+str(dollars['blue'].price)+'\n'
        text=text+dollars['oficial'].name+': '+str(dollars['oficial'].price)
        self.fill_textbox(text)
        

    

def main():
    mi_app = Aplicacion()
    return 0


#__name__ devuelve el nobre del file si estoy en el ejecutor devuelve __main__
if __name__ == '__main__':
    main()

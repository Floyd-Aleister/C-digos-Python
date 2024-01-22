from tkinter import*
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox

self.bt_buscar=Button(self.aba1,text='Buscar',bd=2,bg='#107db2',fg='white'
                               ,font=('verdana',8,'bold'),command=self.janela2)
self.bt_buscar.place(x=100,y=100)#(relx=0.3,rely=0.1,relwidth=0.1,relheight=0.15)
#
root = tix.Tk()
class funcs():
    def limpa_cliente(self):...
    def conecta_bd(self):...
    def desconecta__bd(self):...
    def montaTablas(self):...

    def variaveis(self):...
    def onDoubleClick(self):...
    
    def add_cliente(self):...
    def altera_cliente(self):...
    def deleta_cliente(self):...
    
    def select_lista(self):...
    def busca_cliente(self):...
    def images_base64(self):...

class aplication(funcs, relatorios):

#
    def janela2(self):
        self.root2 = Toplevel()
        self.root2.title('janela2')
        self.root2.configure(background= 'lightblue')
        self.root2.geometry('400x200')
        self.root2.resizable(False, False)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()
        
#

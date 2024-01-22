from tkinter import*
from tkinter import Tk, ttk
from tkinter import messagebox
janela = Tk()
janela.title('Clinica')
janela.geometry('300x200')

########
        #            ==== INICIO ====
       
paisl = Label(janela, text= 'painel',font=('Ivy 23'))
paisl.place(x= 10, y= 10)
#linha
linha = Label(janela,text='',width=600,font=('Ivy 1'),bg='red')
linha.place(x=0,y=50)
#---
paciente = Label(janela, text= 'pacientes cadastrados',font=('Ivy 18'))
paciente.place(x= 20, y= 80)
p_300 = Label(janela, text= '300',font=('Ivy 18'))
p_300.place(x= 60, y= 120)
#
p_adicionados = Label(janela, text= 'Pacientes adicionados',font=('Ivy 18'))
p_adicionados.place(x= 330, y= 80)
p_15 = Label(janela, text= '15',font=('Ivy 18'))
p_15.place(x= 360, y= 120)
#
consulta = Label(janela, text= 'Consultas',font=('Ivy 18'))
consulta.place(x= 20, y= 300)
c_8 = Label(janela, text= '8',font=('Ivy 18'))
c_8.place(x= 60, y= 340)
#
convenio = Label(janela, text= 'Convenios',font=('Ivy 18'))
convenio.place(x= 330, y= 300)
c_18 = Label(janela, text= '18',font=('Ivy 18'))
c_18.place(x= 360, y= 340)

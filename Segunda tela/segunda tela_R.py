from tkinter import*
from tkinter import ttk
janela = Tk()
janela.title('Sistema')
janela.geometry('300x200')

def open():
    window = Tk()
    window.geometry('600x400')


def bt_click():
    consu = Tk()
    consu.title('nova_2')
    consu.geometry('600x600+20+20')

def seg():
    bar = Tk()
    bar.title('nova_3')
    bar.geometry('600x600+20+20')

primeira = Menu(janela)

segunda = Menu(primeira)
#=======
root = Menu(segunda)
#=======

#------------ Tela Produtos -------------
segunda.add_command(label='Agenda',command=open)
#------------ Tela Clientes -------------
segunda.add_command(label='Clientes',command=bt_click)
#
root.add_command(label='Clientes',command=seg)


primeira.add_cascade(label='cadastros',menu=segunda)

primeira.add_cascade(label='Consultas',menu=root)
#segunda.add_cascade(label='Consultas',menu=segunda)
#=======
#menuarquivo = Menu(primeira)
#segunda = Menu(root)
#=======




janela.config(menu=primeira)
janela.mainloop()



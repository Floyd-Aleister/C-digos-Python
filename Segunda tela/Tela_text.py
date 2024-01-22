from tkinter import*
janela = Tk()
janela.title('Sistema')
janela.geometry('300x200')

#===========================================
def open():
    newWindow = Tk()
    newWindow.title('nova')
#===========================================
primeira = Menu(janela)

segunda = Menu(primeira)
#------------ Tela Produtos -------------
segunda.add_command(label='Produtos',command=open)
#------------ Tela Clientes -------------
segunda.add_command(label='Clientes')

primeira.add_cascade(label='cadastros',menu=segunda)

primeira.add_cascade(label='Consultas',menu=segunda)

janela.config(menu=primeira)
janela.mainloop()

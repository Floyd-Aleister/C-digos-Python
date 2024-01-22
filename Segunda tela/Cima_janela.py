from tkinter import*
janela = Tk()
janela.title('Sistema')
janela.geometry('400x400')

primeira = Menu(janela)
segunda = menu=primeira
################ok
primeira = Menu(janela)

segunda = Menu(primeira)
#------------ Tela Produtos -------------
segunda.add_command(label='Produtos')
#------------ Tela Clientes -------------
segunda.add_command(label='Clientes')

primeira.add_cascade(label='cadastros',menu=segunda)

primeira.add_cascade(label='Consultas',menu=segunda)

janela.config(menu=primeira)
janela.mainloop()

from tkinter import*
janela = Tk()
janela.title('Sistema')
janela.geometry('400x300+20+20')

    
#
nome = Label(janela,text='Bem vindo')
nome.pack()
#
et = Entry(janela)
et.pack()

bt = Button(janela,width=20,text='ok')
bt.pack()



    
janela.mainloop()

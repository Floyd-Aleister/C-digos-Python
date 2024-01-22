from tkinter import*
janela = Tk()
janela.geometry('300x300')
#

def deletar():
        
    for widget in janela.winfo_children():
        widget.destroy()
                
    #
    lb = Label(janela,text='SEGUNDA TELA',bg='red').pack()



        
lb = Label(janela, text='PRIMEIRA TELA',bg='blue')
lb.pack()

bt = Button(janela,text='Ok',width=15,command=deletar)
bt.pack()


janela.mainloop()

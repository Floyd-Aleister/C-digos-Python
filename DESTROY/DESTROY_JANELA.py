from tkinter import*
janela = Tk()
janela.geometry('200x200+20+20')
def tela1():
    for widget in janela.winfo_children():
        widget.destroy()
    lb = Label(janela,text='TELA 1',bg='red')
    lb.pack()


        
lb = Label(janela,text='TELA 1',bg='red')
lb.pack()

et = Entry(janela)
et.pack()

bt = Button(janela,text='Ok',command=janela.destroy)
bt.pack()

janela.mainloop()

#----------------------------------------------------------------
janela = Tk()
janela.geometry('200x200+20+20')
    

lb = Label(janela,text='TELA 2',bg='blue')
lb.pack()

et = Entry(janela)
et.pack()

bt = Button(janela,text='Ok',command=janela.destroy)
bt.pack()

janela.mainloop()
#-----------------------------------------------------------------
janela = Tk()
janela.geometry('200x200+20+20')
    

lb = Label(janela,text='TELA 3',bg='yellow').pack()

et = Entry(janela)
et.pack()

bt = Button(janela,text='Ok',command=tela1)
bt.pack()

janela.mainloop()
#-----------------------------------------------------------------

janela = Tk()
janela.geometry('200x200+20+20')
    

lb = Label(janela,text='TELA 4')
lb.pack()

et = Entry(janela)
et.pack()

bt = Button(janela,text='Ok',command=janela.destroy)
bt.pack()

janela.mainloop()
#-------------------------------------------------------------------

janela = Tk()
janela.geometry('200x200+20+20')
    

lb = Label(janela,text='TELA 5')
lb.pack()

et = Entry(janela)
et.pack()

bt = Button(janela,text='Ok',command=janela.destroy)
bt.pack()

janela.mainloop()

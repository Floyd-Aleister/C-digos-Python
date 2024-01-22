from tkinter import *

janela = Tk()
janela.title('Sistema')
janela.geometry('300x300+200+200')


def bt1_click():
    print('primeiro botão')

    lb['text'] = 'A = 30, e B = 10'
    

def bt2_click():
    print('segundo botão')

    lb['text'] = 'A = 10, e B = 30'

    
bt1 = Button(janela, width=20, text='Ok',command= bt1_click )
bt1.place(x=100, y=100)

bt2 = Button(janela, width=20, text='Exemplo',command= bt2_click )
bt2.place(x=100, y=150)

lb = Label(janela, text='A = 10, e B = 30')
lb.place(x=100, y=180)








janela.mainloop()

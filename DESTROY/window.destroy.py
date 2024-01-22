from tkinter import*
window = Tk()
window.geometry('200x200')
    



lb = Label(window,text='Ola')
lb.pack()

et = Entry(window)
et.pack()


bt = Button(window,text='Ok',command=window.destroy)
bt.pack()


window.mainloop()

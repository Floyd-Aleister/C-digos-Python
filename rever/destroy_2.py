from tkinter import*
root = Tk()
root.title('codemy')
root.geometry('400x400')
bl = Label(root,text='sistema')
my_menu = Menu(root)
root.config(menu=my_menu)

def our_command():
    my_label = Label(root,text='you!').pack()

def file_new():
    hide_all_frames()
    file_new_frame.pack(fill='both',expand=1)
    my_label = Label(file_new_frame,text='file')

file_menu = Menu(my_menu)
my_menu.add_cascade(bl,menu=file_menu)
file_menu.add_command(command=file_new)
file_menu.add_separator()
file_menu.add_command(Label='Exit',command=root.quit)

root.mainloop()

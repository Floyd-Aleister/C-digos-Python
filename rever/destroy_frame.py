from tkinter import*
root = Tk()
root.title('codemy')
root.geometry('400x400')

my_menu = Menu(root)
root.config(menu=my_menu)

def our_command():
    my_label = Label(root,text='you!').pack()

def file_new():
    hide_all_frames()
    file_new_frame.pack(fill='both',expand=1)
    my_label = Label(file_new_frame,text='file')

def edit_cut():
    hide_all_frame()
    edit_cut_frame.pack(fill='both',expand=1)
    my_label = Label(edit_cut_freme,text='cut')

def hide_all_frames():
    for widget in file_new_frame.winfo_children():
        widget.destroy()
        
    for widget in edit_cut_frame.winfo_children():
        widget.destroy()
    
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()
    
   # file_new_frame.pack()
   # edit_cut_frame.pack()
    
file_menu = Menu(my_menu)
my_menu.add_cascade(Label='File',menu=file_menu)
file_menu.add_command(Label='New...',command=file_new)
file_menu.add_separator()
file_menu.add_command(Label='Exit',command=root.quit)
#
edit_menu = Menu(my_menu)
my_menu.add_cascade(Label='Edit',menu=edit_menu)
edit_menu.add_command(Label='Cut',command=edit_cut)
edit_menu.add_command(Label='Copy',command=our_command)
#
option_menu = Menu(my_menu)
my_menu.add_cascade(Label='Options',menu=optin_menu)
option_menu.add_command(Label='Find',command=our_command)
option_menu.add_command(Label='Find Next',command=our_command)

file_new_frame = Frame(root,width=400,height=400,bg='red')
edit_cut_frame = Frame(root,width=400,height=400,bg='blue')

root.mainloop()









from tkinter import*
from tkinter import ttk
janela = Tk()
janela.title('Sistema')
janela.geometry('600x600')

def open():
    newWindow = Tk()
    newWindow.title('nova')
    newWindow.geometry('600x600+20+20')
   
def bt_click():
    consu = Tk()
    consu.title('nova_2')
    consu.geometry('600x600+20+20')

def seg():
    janela = Tk()
    janela.title('nova_3')
    janela.geometry('600x600+20+20')
#            ==== INICIO ====    
    codigo_lb = Label(janela, text= 'Código')
    codigo_lb.place(x= 10, y= 10)

    nome_lb = Label(janela, text= 'Nome')
    nome_lb.place(x= 10, y= 40)

    data_lb = Label(janela, text= 'Data Nasc.')
    data_lb.place(x= 10, y= 70)

    sexo_lb = Label(janela, text= 'Sexo')
    sexo_lb.place(x= 220, y= 70)

    telefone_lb = Label(janela, text= 'Telefone')
    telefone_lb.place(x= 10, y=100)

    celular_lb = Label(janela, text='Celular')
    celular_lb.place(x= 220, y=100)

    rg_lb = Label(janela, text= 'RG')
    rg_lb.place(x= 10, y= 130)

    cpf_lb = Label(janela, text= 'CPF')
    cpf_lb.place(x=10, y= 160)

    endereço_lb = Label(janela, text= 'Endereço')
    endereço_lb.place(x= 10, y= 190)

    pai_lb = Label(janela, text= 'Pai')
    pai_lb.place(x=10, y= 290)

    mae_lb = Label(janela, text= 'Mãe')
    mae_lb.place(x= 300, y= 290)

    email_lb = Label(janela, text= 'E-mail')
    email_lb.place(x= 10, y= 320)

    observ_lb = Label(janela, text= 'Observações')
    observ_lb.place(x= 10, y= 350)


#================= Entrdas ========================
    codigo_en = Entry(janela, width= 18)
    codigo_en.place(x= 100, y= 10)

    empresa = Checkbutton(janela, text= 'Empresa').place(x=220,y=10)

    nome_en = Entry(janela, width= 44)
    nome_en.place(x= 100, y= 40)
#------------------ Lista1 --------------------
    listaData = ['20','30','40']

    data_en = ttk.Combobox(janela, width= 15, values=listaData,state='readonly')
    data_en.place(x= 100, y= 70)
#------------------ Lista2 --------------------

    listaSexo = ['Masculino','Feminino']

    sexo_en = ttk.Combobox(janela, width= 15, values=listaSexo,state='readonly')
    sexo_en.place(x= 255, y= 70)

    telefone_en = Entry(janela, width= 18)
    telefone_en.place(x=100, y= 100)
#celular
    cel = Entry(janela, width= 16)
    cel.place(x= 270, y= 100)

    rg_ent = Entry(janela, width= 18)
    rg_ent.place(x= 100, y= 130)
#
    produto = Checkbutton(janela, text= 'Produtor Rural')
    produto.place(x= 220, y= 130)
#
    cpf_ent = Entry(janela, width= 18)
    cpf_ent.place(x= 100, y= 160)
#========
    endereço = Listbox(janela, width= 70,height =5, bg='white')
    endereço.place(x= 100, y= 190)

#endereço = Entry(Listbox(janela, width= 70,height =5, bg='white'))
#endereço.place(x= 100, y= 190)
#========
    pai_ent = Entry(janela, width= 30)
    pai_ent.place(x= 100, y= 290)

    mae_ent = Entry(janela, width= 30)
    mae_ent.place(x= 335, y= 290)

    email_ent = Entry(janela, width= 44)
    email_ent.place(x= 100, y= 320)

    obser_ent = Listbox(janela, width=70,height = 3, bg='white')
    obser_ent.place(x= 100, y= 350)
#
    salvarlb = Label(janela,width=7,font= 'Arial 30 bold',bg= '#8FBC8F')
    salvarlb.place(x=100, y=470)

    salvarbt = Button(janela,width=10,text= 'Salvar',font= 'Arial 15 bold',fg= 'black')
    salvarbt.place(x=122, y=474)

    cancelarlb = Label(janela,width=7,font= 'Arial 30 bold',bg= '#8FBC8F')
    cancelarlb.place(x=300, y=470)

    cancelarbt = Button(janela,width=10,text='cancelar',font='Arial 15 bold',fg= 'black')
    cancelarbt.place(x=322, y=474)
#                      ===== FIM=======

primeira = Menu(janela)

segunda = Menu(primeira)
#=======
root = Menu(segunda)
#=======

#------------ Tela Produtos -------------
segunda.add_command(label='Produtos',command=open)
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



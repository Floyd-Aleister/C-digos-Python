from tkinter import*
from tkinter import ttk
janela = Tk()
janela.title('Sistema')
janela.geometry('600x600')

paisl = Label(janela, text= 'painel',font=('Ivy 23'))
paisl.place(x= 10, y= 10)
#linha
linha = Label(janela,text='',width=600,font=('Ivy 1'),bg='red')
linha.place(x=0,y=50)
#---
paciente = Label(janela, text= 'pacientes cadastrados',font=('Ivy 18'))
paciente.place(x= 20, y= 80)
p_300 = Label(janela, text= '300',font=('Ivy 18'))
p_300.place(x= 60, y= 120)
#
p_adicionados = Label(janela, text= 'Pacientes adicionados',font=('Ivy 18'))
p_adicionados.place(x= 330, y= 80)
p_15 = Label(janela, text= '15',font=('Ivy 18'))
p_15.place(x= 360, y= 120)
#
consulta = Label(janela, text= 'Consultas',font=('Ivy 18'))
consulta.place(x= 20, y= 300)
c_8 = Label(janela, text= '8',font=('Ivy 18'))
c_8.place(x= 60, y= 340)
#
convenio = Label(janela, text= 'Convenios',font=('Ivy 18'))
convenio.place(x= 330, y= 300)
c_18 = Label(janela, text= '18',font=('Ivy 18'))
c_18.place(x= 360, y= 340)

def open():
    newWindow = Tk()
    newWindow.title('nova')
    newWindow.geometry('600x600+20+20')
#################### segunda janela ############################  
def bt_click():
   #====================== Label ===========================
    paisl = Label(janela, text= 'País')
    paisl.place(x= 10, y= 20)

    cepl = Label(janela, text= 'CEP')
    cepl.place(x= 10, y= 50)

    uf = Label(janela, text= 'UF')
    uf.place(x= 230, y= 50)

    endereço_l = Label(janela, text= 'Endereço')
    endereço_l.place(x= 10, y= 80)

    numero_l = Label(janela, text= 'Número')
    numero_l.place(x= 10, y= 110)

    complemento = Label(janela, text= 'Complemento')
    complemento.place(x= 240, y= 110)

    bairro_l = Label(janela, text= 'Bairro')
    bairro_l.place(x= 10, y= 140)

    codigo_l = Label(janela, text= 'Código Mun.')
    codigo_l.place(x= 10, y= 170)

    codigo_lb = Label(janela, text= 'Código IBGE para o município')
    codigo_lb.place(x= 240, y= 170)

    cidade = Label(janela, text= 'Cidade')
    cidade.place(x= 10, y= 200)

    destinatario = Label(janela, text= 'Destinatário')
    destinatario.place(x= 10, y= 230)

    obs_l = Label(janela, text= 'Obs:')
    obs_l.place(x= 10, y= 260)

#============================ Entradas =================================


#--------------------- 1ista1 ---------------------
    listaPais = ['Brasil','Irâ','Portugal']

    pais_en = ttk.Combobox(janela, width= 62,values=listaPais,state='readonly')
    pais_en.set('Brasil')
    pais_en.place(x= 100, y=20)


    cepe = Entry(janela,)
    cepe.place(x= 100, y= 50)

#--------------------- lista2 --------------------
    listaEstados = ['Selecione','PE','AL','PB','SE','RN','CE']

    uf_estados = ttk.Combobox(janela,width=10, values=listaEstados,state='readonly')
    uf_estados.set('Selecione')
    uf_estados.place(x=250, y=50)

    endereço_e = Entry(janela, width= 65)
    endereço_e.place(x=100, y= 80)

    numero_e = Entry(janela)
    numero_e.place(x= 100, y= 110)

    complemento_e = Entry(janela)
    complemento_e.place(x= 325, y= 110)
#--------------------- lista3 ---------------------
    listaBairros = ['Divinópolis','Petrópolis','Rendeiras']

    cb_Bairros = ttk.Combobox(janela,width=62, values=listaBairros,state='readonly')
#cb_Bairros.set('Selecione')
    cb_Bairros.place(x=100, y=140)
#
    codigo_m = Entry(janela)
    codigo_m.place(x= 100, y= 170)

#--------------------- lista4 ----------------------
    listaCidades = ['Caruaru','Recife']
    ent_Cidade = ttk.Combobox(janela,width=40, values=listaCidades,state='readonly')
    ent_Cidade.place(x= 100, y= 200)

    destinatario_e = Entry(janela, width= 65)
    destinatario_e.place(x= 100, y= 230)

    obs_e = Entry(janela, width= 65)
    obs_e.place(x= 100, y= 260)


#Deixar letras claras , cor e imagens no Entry
#janela.mainloop()

def seg():
    janela =Tk.destroy()
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
segunda.add_command(label='agenda',command=open)
#------------ Tela Clientes -------------
segunda.add_command(label='Clientes',command=bt_click)
#******************************
root.add_command(label='Clientes',command=seg)
primeira.add_cascade(label='               ')
#*                                      ##############
primeira.add_cascade(label='Agenda',font=('Ivy 10'),menu=segunda)
#####
#####
primeira.add_cascade(label='Consultas',menu=root)
#segunda.add_cascade(label='Consultas',menu=segunda)
#=======
#menuarquivo = Menu(primeira)
#segunda = Menu(root)
#=======

janela.config(menu=primeira)
janela.mainloop()



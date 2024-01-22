from tkinter import*
from tkinter import ttk
janela = Tk()
janela.title('Exemplo')
janela.geometry('600x600')

lb_cadastro = Label(janela,text='Cadastro do paciente',font=('Ivy 23'))
lb_cadastro.place(x= 10, y= 10)

linha = Label(janela,text='',width=600,font=('Ivy 1'),bg='red').place(x=0,y=50)

lb_dados = Label(janela, text= 'Dados pessoais',font=('Ivy 15'))
lb_dados.place(x= 10, y= 70)
        
lb_nome = Label(janela, text= 'Nome completo')
lb_nome.place(x= 10, y= 100)
#
et_nome = Entry(janela,width=60).place(x=10, y= 120)

lb_data = Label(janela,text='Data de nascimento').place(x=430, y=100)
et_data = Entry(janela,width=20).place(x=430, y= 120)

lb_cor = Label(janela, text= 'Cor').place(x= 10, y= 140)
et_cor = Entry(janela).place(x=10, y= 160)

lb_estado_c = Label(janela, text= 'Estado civil').place(x= 180, y=140)
#
et_estado_c = Entry(janela).place(x=180, y=160)

lb_natural = Label(janela, text='Naturalidade').place(x= 350, y=140)
#
et_natural = Entry(janela,width=30).place(x=350, y=160)

rg_lb = Label(janela, text= 'RG').place(x= 10, y= 180)
#
rg_lb = Entry(janela,width= 35).place(x=10, y=200)
#emissor
lb_emissor = Label(janela,text='Emissor').place(x=250 ,y=180)
et_emissor = Entry(janela,width=10).place(x=250 , y=200)
                                                
cpf_lb = Label(janela, text= 'CPF').place(x=340, y= 180)
cpf_et = Entry(janela,width=35).place(x=340, y=200)

lb_email = Label(janela,text='E-mail').place(x=10 , y=220)
et_email = Entry(janela,width=50).place(x=10 ,y=240 )
##########--- lista 1--------------------------
listaCidade = ['Caruaru','Recife']

lb_cidade = Label(janela,text='Cidade').place(x=10 ,y=260)
et_cidade = ttk.Combobox(janela,width=35,values=listaCidade,state='readonly').place(x=10 , y=280)
##########--- lista 2-----------------------------
listaBairro = ['Petrópolis','Divinópolis','Cidade jardim']

lb_bairro = Label(janela,text='Bairro').place(x=290 , y=260)
et_bairro = ttk.Combobox(janela,width=40, values=listaBairro,state='readonly').place(x=290 ,y=280)
########-------------------------------------
lb_cep = Label(janela,text='Cep').place(x=10 , y=304)
et_cep = Entry(janela,width=35).place(x=10 ,y=324)
########----- lista 3--------------------------------
listaEstados = ['Alagoas','Pernanbuco','Cergipe']

lb_estado = Label(janela,text='Estado').place(x=290 , y=304)
et_estado = ttk.Combobox(janela,width=40, values=listaEstados,state='readonly').place(x=290 , y=324)
#########
lb_numero = Label(janela,text='Numero:').place(x=10 ,y=345)
et_numero = Entry(janela,width=40).place(x=10, y=365)



janela.mainloop()

from tkinter import*


class Gui():
    """docstring for Gui"""
    # Variaveis para psocionamento e tamanho de componentes
    x_pad = 5
    y_pad = 3
    width_entry = 30

    # criando a janela
    window = Tk()
    window.wm_title("Cadastro de Clientes")

    # Variaveis para entrada de dados
    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar()

    # Labels para as entradas de dados
    lblnome = Label(window, text="Nome")
    lblsobrenome = Label(window, text="Sobrenome")
    lblemail = Label(window, text="Email")
    lblCPF = Label(window, text="CPF")

    # Entrada de dados via Entry()
    entNome = Entry(window, textvariable=txtNome)
    entSobrenome = Entry(window, textvariable=txtSobrenome)
    entEmail = Entry(window, textvariable=txtEmail)
    entCPF = Entry(window, textvariable=txtCPF)

    # Criação da lista de Clientes e da scrollBar
    listClientes = Listbox(window, width=50)
    scrollClientes = Scrollbar(window)

    # Botões, apenas a criação, sem posicionar
    btnViewAll = Button(window, text="Ver todos")
    btnSearch = Button(window, text="Buscar")
    btnInsert = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar Selecionados")
    btnDelete = Button(window, text="Deletar Selecionados")
    btnClose = Button(window, text="Fechar")

    # Posiocionando todos os objetos no grid da Janela
    lblnome.grid(row=0, column=0)
    lblsobrenome.grid(row=1, column=0)
    lblemail.grid(row=2, column=0)
    lblCPF.grid(row=3, column=0)

    entNome.grid(row=0, column=1, padx=50, pady=50)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)

    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnSearch.grid(row=5, column=0, columnspan=2)
    btnInsert.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDelete.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

    # Ligando o Scrollbar ao Listbox
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    # Correção no posicionamento e tamanho dos objetos
    # de forma iterativa, passando as configurações usando um for

    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')

    def run(self):
        Gui.window.mainloop()
        #Gui.window.wm_minsize(10, 10)

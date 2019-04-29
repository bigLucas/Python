from gui import*
import backend as core

app = None


def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)


def search_command():
    app.listClientes.delete(0, END)
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(),
                       app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, r)


def insert_command():
    core.insert(app.txtNome.get(), app.txtSobrenome.get(),
                app.txtEmail.get(), app.txtCPF.get())
    view_command()


def update_command():
    core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(
    ), app.txtEmail.get(), app.txtCPF.get())
    view_command()


def delete_command():
    id = selected[0]
    core.delete(id)
    view_command()


def getSelectedRow(event):
    # Variavel global, pode ser acessada em qualquer ponto do script
    global selected
    # Nessa etapa é recuperado o indice do item na listbox
    # apos isso a listbox é preenchida com novos valores
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)
    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entSobrenome.delete(0, END)
    app.entSobrenome.insert(END, selected[2])
    app.entEmail.delete(0, END)
    app.entEmail.insert(END, selected[3])
    app.entCPF.delete(0, END)
    app.entCPF.insert(END, selected[4])


if __name__ == "__main__":
    # Atribui a interface grafica a variavel app
    app = Gui()
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)
    # Relaciona os botoes para cada chamada de função
    app.btnViewAll.configure(command=view_command)
    app.btnSearch.configure(command=search_command)
    app.btnInsert.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDelete.configure(command=delete_command)
    app.btnClose.configure(command=app.window.destroy)

    app.run()

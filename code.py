import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

def carregar_dados():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            return json.load(f)
    else:
        return []

def salvar_dados(users):
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)

def adicionar_usuario():
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()

    if nome and idade and email:
        users = carregar_dados()
        users.append({"nome": nome, "idade": idade, "email": email})
        salvar_dados(users)
        exibir_usuarios()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
    else:
        messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos.")

def exibir_usuarios(filtro=None):
    users = carregar_dados()
    listbox_usuarios.delete(0, tk.END) 

    if filtro:
        users = [user for user in users if filtro.lower() in user['nome'].lower() or filtro.lower() in user['email'].lower()]
    
    for user in users:
        listbox_usuarios.insert(tk.END, f"Nome: {user['nome']} | Idade: {user['idade']} | E-mail: {user['email']}")

def atualizar_usuario():
    try:
        selected_index = listbox_usuarios.curselection()[0]
        nome = entry_nome.get()
        idade = entry_idade.get()
        email = entry_email.get()

        if nome and idade and email:
            users = carregar_dados()
            users[selected_index] = {"nome": nome, "idade": idade, "email": email}
            salvar_dados(users)
            exibir_usuarios()
            limpar_campos()
            messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, preencha todos os campos.")
    except IndexError:
        messagebox.showwarning("Seleção inválida", "Por favor, selecione um usuário para atualizar.")

def excluir_usuario():
    try:
        selected_index = listbox_usuarios.curselection()[0]
        users = carregar_dados()
        del users[selected_index]
        salvar_dados(users)
        exibir_usuarios()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
    except IndexError:
        messagebox.showwarning("Seleção inválida", "Por favor, selecione um usuário para excluir.")

def buscar_usuarios():
    filtro = entry_busca.get()
    exibir_usuarios(filtro)

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_busca.delete(0, tk.END)

root = tk.Tk()
root.title("Sistema CRUD de Usuários")
root.geometry("700x500")

label_titulo = tk.Label(root, text="Cadastro de Usuários", font=("Arial", 16, "bold"))
label_titulo.pack(pady=20)

frame_campos = tk.Frame(root)
frame_campos.pack(pady=10)

label_nome = tk.Label(frame_campos, text="Nome:", font=("Arial", 10))
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(frame_campos, font=("Arial", 10))
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_idade = tk.Label(frame_campos, text="Idade:", font=("Arial", 10))
label_idade.grid(row=1, column=0, padx=10, pady=5)
entry_idade = tk.Entry(frame_campos, font=("Arial", 10))
entry_idade.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(frame_campos, text="E-mail:", font=("Arial", 10))
label_email.grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(frame_campos, font=("Arial", 10))
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_busca = tk.Label(root, text="Buscar por nome ou e-mail:", font=("Arial", 10))
label_busca.pack(pady=5)
entry_busca = tk.Entry(root, font=("Arial", 10))
entry_busca.pack(pady=5)
button_buscar = tk.Button(root, text="Buscar", font=("Arial", 10), command=buscar_usuarios)
button_buscar.pack(pady=5)

frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=20)

button_adicionar = tk.Button(frame_botoes, text="Adicionar", font=("Arial", 12), command=adicionar_usuario, width=12)
button_adicionar.grid(row=0, column=0, padx=10)

button_atualizar = tk.Button(frame_botoes, text="Atualizar", font=("Arial", 12), command=atualizar_usuario, width=12)
button_atualizar.grid(row=0, column=1, padx=10)

button_excluir = tk.Button(frame_botoes, text="Excluir", font=("Arial", 12), command=excluir_usuario, width=12)
button_excluir.grid(row=0, column=2, padx=10)

frame_listbox = tk.Frame(root)
frame_listbox.pack(pady=10)

listbox_usuarios = tk.Listbox(frame_listbox, width=80, height=10, font=("Arial", 10), selectmode=tk.SINGLE)
listbox_usuarios.pack(pady=10)
exibir_usuarios()

root.mainloop()

from conexao import Conexao as Conn
import tkinter as tk
from tkinter import messagebox

nova_conexao = Conn("Projeto 7/database.db", "", "")

def cadastrar_aluno():
    nome = nome_entry.get()
    first = first_entry.get()
    last = last_entry.get()
    idade = int(idade_entry.get())
    telefone = int(telefone_entry.get())
    media = int(media_entry.get())

    cadastro = nova_conexao.inserir_dado(first, last, nome, idade, telefone, media)

    result_text.delete(1.0, tk.END)
    
    messagebox.showinfo("Cadastro de Aluno", cadastro)

def ver_lista_alunos():
    dados = nova_conexao.consultar_tabela()
    
    result_text.delete(1.0, tk.END)
    
    for dado in dados:
        result_text.insert(tk.END, f"ID: {dado[0]}\n")
        result_text.insert(tk.END, f"Primeiro nome: {dado[1]}\n")
        result_text.insert(tk.END, f"Último nome: {dado[2]}\n")
        result_text.insert(tk.END, f"Nome completo: {dado[3]}\n")
        result_text.insert(tk.END, f"Idade: {dado[4]}\n\n")
        result_text.insert(tk.END, f"Telefone: {dado[5]}\n\n")
        result_text.insert(tk.END, f"Média: {dado[6]}\n\n")

def consultar_aluno():
    id_aluno = int(consulta_entry.get())
    
    dados = nova_conexao.consultar_dado(id_aluno)
    
    if dados:
        result_text.delete(1.0, tk.END)

        for dado in dados:
            result_text.insert(tk.END, f"ID: {dado[0]}\n")
            result_text.insert(tk.END, f"Primeiro nome: {dado[1]}\n")
            result_text.insert(tk.END, f"Último nome: {dado[2]}\n")
            result_text.insert(tk.END, f"Nome completo: {dado[3]}\n")
            result_text.insert(tk.END, f"Idade: {dado[4]}\n\n")
            result_text.insert(tk.END, f"Telefone: {dado[5]}\n\n")
            result_text.insert(tk.END, f"Média: {dado[6]}\n\n")
    else:
        messagebox.showwarning("Consulta de Aluno", "Aluno não encontrado!")

# Cria a janela principal
root = tk.Tk()
root.title("Cadastrador de Alunos")
root.geometry("668x500")
root.resizable(False, False)

label_nome = tk.Label(root, text="Nome Completo:")
nome_entry = tk.Entry(root)

label_first = tk.Label(root, text="Primeiro Nome:")
first_entry = tk.Entry(root)

label_last = tk.Label(root, text="Último Nome:")
last_entry = tk.Entry(root)

label_idade = tk.Label(root, text="Idade:")
idade_entry = tk.Entry(root)

label_media = tk.Label(root, text="Nota Média:")
media_entry = tk.Entry(root)

label_telefone = tk.Label(root, text="Telefone do Aluno:")
telefone_entry = tk.Entry(root)

cadastrar_button = tk.Button(root, text="Cadastrar", command=cadastrar_aluno)
listar_button = tk.Button(root, text="Ver Lista de Alunos", command=ver_lista_alunos)

label_consulta = tk.Label(root, text="Consultar Aluno por ID:")
consulta_entry = tk.Entry(root)
consultar_button = tk.Button(root, text="Consultar", command=consultar_aluno)

result_text = tk.Text(root, height=10, width=50)

label_nome.grid(row=0, column=0, padx=5)
nome_entry.grid(row=1, column=0, padx=5)

label_first.grid(row=0, column=1)
first_entry.grid(row=1, column=1)

label_last.grid(row=0, column=2)
last_entry.grid(row=1, column=2)

label_idade.grid(row=2, column=0)
idade_entry.grid(row=3, column=0)

label_media.grid(row=2, column=1)
media_entry.grid(row=3, column=1)

label_telefone.grid(row=2, column=2)
telefone_entry.grid(row=3, column=2)

cadastrar_button.grid(row=4, column=1)

listar_button.grid(row=5, column=1)

label_consulta.grid(row=6, column=1)
consulta_entry.grid(row=7, column=1)
consultar_button.grid(row=8, column=1)

result_text.grid(row=9, column=1)

root.mainloop()

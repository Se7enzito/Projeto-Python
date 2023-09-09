from tkinter import *

janela = Tk()
janela.geometry("310x400")
janela.title("Calculadora")
janela.resizable(False, False)

visor = Entry(font=("Arial", 20), borderwidth=5, justify="right", bg="pink", fg="black", validate="key")
visor.grid(row=0, column=0, columnspan=4)

def clicar(num):
    if (num == "C"):
        visor.delete(0, END)
    else:
        atual = visor.get()
        visor.delete(0, END)
        visor.insert(0, atual + str(num))

def calcular():
    try:
        resultado = eval(visor.get())
        visor.delete(0, END)
        visor.insert(0, str(resultado))
    except Exception as e:
        visor.delete(0, END)
        visor.insert(0, "Erro")

def validate_input(P):
    valid_chars = "0123456789+-*/.()"  # Caracteres válidos
    if all(char in valid_chars for char in P):
        return True
    else:
        return False

validate_func = janela.register(validate_input)
visor.config(validate="key", validatecommand=(validate_func, "%P"))

botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (texto, linha, coluna) in botoes:
    botao = Button(janela, text=texto, padx=20, pady=20, font=("Arial", 16), fg="yellow", bg="blue", command=lambda t=texto: clicar(t) if t != "=" else calcular())
    botao.grid(row=linha, column=coluna)

janela.mainloop()
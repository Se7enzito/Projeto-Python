from tkinter import *

janela = Tk()
janela.geometry("300x300")

n1 = Label(text="Número 1")
n1.pack()

entry1 = Entry(validate="key")
entry1.pack()

n2 = Label(text="Número 2")
n2.pack()

entry2 = Entry(validate="key")
entry2.pack()

adicao = Button(text="Adição", command=lambda: [print(f"{int(entry1.get()) + int(entry2.get())}")])
adicao.pack()

sub = Button(text="Subtração", command=lambda: [print(f"{int(entry1.get()) - int(entry2.get())}")])
sub.pack()

div = Button(text="Divisão", command=lambda: [print(f"{int(entry1.get()) / int(entry2.get())}")])
div.pack()

mult = Button(text="Multiplicação", command=lambda: [print(f"{int(entry1.get()) * int(entry2.get())}")])
mult.pack()

def validate_input(P):
    if P.isdigit():
        return True
    else:
        return False
    
validate_func = janela.register(validate_input)
entry1.config(validate="key", validatecommand=(validate_func, "%P"))

janela.mainloop()
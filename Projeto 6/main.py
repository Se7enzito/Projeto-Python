from tkinter import *

janela = Tk()
janela.geometry("370x400")
janela.title("Conversor")
# janela.resizable(False, False)

tcelcius = Label(text="Celcius")
tfahrenheit = Label(text="Fahrenheit")
tkelvin = Label(text="Kelvin")

celcius = Entry()
fahrenheit = Entry()
kelvin = Entry()

resultado = Label()

def converter():
    try:
        if celcius.get():
            celsius_temp = float(celcius.get())
            fahrenheit_temp = (celsius_temp * 9/5) + 32
            kelvin_temp = celsius_temp + 273.15
            resultado.config(text=f"Fahrenheit: {fahrenheit_temp:.2f}°F, Kelvin: {kelvin_temp:.2f}K")
        elif fahrenheit.get():
            fahrenheit_temp = float(fahrenheit.get())
            celsius_temp = (fahrenheit_temp - 32) * 5/9
            kelvin_temp = (fahrenheit_temp - 32) * 5/9 + 273.15
            resultado.config(text=f"Celsius: {celsius_temp:.2f}°C, Kelvin: {kelvin_temp:.2f}K")
        elif kelvin.get():
            kelvin_temp = float(kelvin.get())
            celsius_temp = kelvin_temp - 273.15
            fahrenheit_temp = (kelvin_temp - 273.15) * 9/5 + 32
            resultado.config(text=f"Celsius: {celsius_temp:.2f}°C, Fahrenheit: {fahrenheit_temp:.2f}°F")
    except ValueError:
        resultado.config(text="Insira um valor válido")

converte = Button(text="Conversão", command=converter)
limpar = Button(text="Limpar", command=lambda: [celcius.delete(0, END), fahrenheit.delete(0, END), kelvin.delete(0, END), resultado.config(text="")])

tcelcius.grid(row=0, column=0)
tfahrenheit.grid(row=0, column=1)
tkelvin.grid(row=0, column=2)
celcius.grid(row=1, column=0)
fahrenheit.grid(row=1, column=1)
kelvin.grid(row=1, column=2)
converte.grid(row=2, column=0)
limpar.grid(row=2, column=1)
resultado.grid(row=3, columnspan=3)

janela.mainloop()
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida!"
    return a / b

def resto(a, b):
    return a % b

def pot(a, b):
    return a ** b

def menu():
    print("Escolha a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Resto")
    print("6 - Potência")
    print("7 - Sair")

while True:
    menu()
    opcao = input("Digite o número da operação desejada: ")

    if opcao == "7":
        print("Calculadora encerrada.")
        break

    if opcao not in ("1", "2", "3", "4", "5", "6"):
        print("Opção inválida. Escolha uma das opções válidas.")
        continue

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        print("Resultado: ", somar(numero1, numero2))
    elif opcao == "2":
        print("Resultado: ", subtrair(numero1, numero2))
    elif opcao == "3":
        print("Resultado: ", multiplicar(numero1, numero2))
    elif opcao == "4":
        print("Resultado: ", dividir(numero1, numero2))
    elif opcao == "5":
        print("Resultado: ", resto(numero1, numero2))
    elif opcao == "6":
        print("Resultado: ", pot(numero1, numero2))
    
    print('\n')
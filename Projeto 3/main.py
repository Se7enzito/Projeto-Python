# Pedra papel tesoura
import random

def obter_escolha_usuario():
    while True:
        escolha = input("Escolha pedra, papel ou tesoura: ").lower()
        if escolha in ["pedra", "papel", "tesoura"]:
            return escolha
        print("Escolha inválida. Tente novamente.")

def obter_escolha_computador():
    return random.choice(["pedra", "papel", "tesoura"])

def determinar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate"
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        return "Você venceu!"
    else:
        return "O computador venceu!"

def jogar_pedra_papel_tesoura():
    escolha_usuario = obter_escolha_usuario()
    escolha_computador = obter_escolha_computador()
    print(f"Você escolheu: {escolha_usuario}")
    print(f"O computador escolheu: {escolha_computador}")
    resultado = determinar_vencedor(escolha_usuario, escolha_computador)
    print(resultado)

jogar_pedra_papel_tesoura()
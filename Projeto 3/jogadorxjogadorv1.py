# Criando a classe jogador para fazer um POO
class Jogador():
    def __init__(self, nome, escolha): # Falando que o jogador pode conter um nome e uma escolha
        self._nome = nome # Seta o nome
        self._escolha = escolha # Seta a escolha

    @property # Fala que é uma propriedade
    def escolha(self): # Cria a função para retornar a escolha
        return self._escolha # Retorna qual a escolha
    
    @property # Fala que é uma propriedade
    def nome(self): # Cria a função para retornar o nome
        return self._nome # Retorna qual o nome
    
# Cria a função para obter a escolha do usuário
def obter_escolha_usuario():
    while True: # Cria um looping
        escolha = input("Escolha pedra, papel ou tesoura: ").lower() # Pede uma escolha e coloca ela em lowercase para ficar tudo padrão
        if escolha in ["pedra", "papel", "tesoura"]: # Ve se a escolha é uma das listadas
            return escolha # Retorna a escolha ao código
        print("Escolha inválida. Tente novamente.") # Pede outra escolha
        
# Cria a função para pegar o nome do jogador
def obter_nome():
    nome = input("Qual o seu nome? ") # Perguntando o nome do jogador
        
    return nome # Retornando o nome do jogador
        
# Cria a função para obter o vencedor
def determinar_vencedor(escolha_usuario0, escolha_usuario1, nome_usuario0, nome_usario1):
    if escolha_usuario0 == escolha_usuario1: # Se as escolhas fdorem iguais determina que é um empate
        return "Empate" # Retorna falando que foi um empate
    # Confere todos cenários possiveis de vitória
    elif (escolha_usuario0 == "pedra" and escolha_usuario1 == "tesoura") or \
         (escolha_usuario0 == "papel" and escolha_usuario1 == "pedra") or \
         (escolha_usuario0 == "tesoura" and escolha_usuario1 == "papel"):
        return f"O jogador {nome_usuario0} ganhou!" # Retorna que o user 2 ganhou
    else: # Se o user 0 não ganhar o user 1 ganha
        return f"O jogador {nome_usario1} ganhou!" # Retorna que o user 1 ganhou

# Cria uma metodo finalizador
quer_jogar = input("Vocês querem jogar uma partida? (Sim para jogar)")

# Faz uma if para precisar enviar o nome so uma vez
if (quer_jogar.lower() == "sim"):
    nome0 = obter_nome() # Pergunta o nome do jogador
    nome1 = obter_nome() # Pergunta o nome do jogador

# Confere se o metodo esta ok
while quer_jogar.lower() == "sim":
    # Setando os jogadores
    jogador0 = Jogador(nome0, obter_escolha_usuario())
    jogador1 = Jogador(nome1, obter_escolha_usuario())

    # Apenas debug:
    # print(jogador1.nome)
    # print(jogador1.escolha)
    # print(jogador2.nome)
    # print(jogador2.escolha)

    # Chama a função para ver quem vai ganhar
    print(determinar_vencedor(jogador0.escolha, jogador1.escolha, jogador0.nome, jogador1.nome))
    
    # Pergunta se querem jogar mais uma partida
    quer_jogar = input("Vocês querem jogar mais uma partida? (Sim para jogar) ")
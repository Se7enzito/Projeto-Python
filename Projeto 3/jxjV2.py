# Importa biblioteca
import tkinter as tk

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

vitorias = {} # Cria um dicionário para armazenar as vitórias
escolha_do_usuario = None  # Variável para armazenar a escolha do jogador

# Criando a classe de janela para fazer um POO
class EscolhaJanela(tk.Tk):
    def __init__(self, nome): # Falando que tem o nome do jogador na janela
        super().__init__() # Inicia o __init__
        self.title(f"Escolha do {nome}") # Cria o nome da janela
        self.escolha_do_usuario = None # Seta escolha do jogador como nenhuma

        botao_pedra = tk.Button(self, text="Pedra", command=lambda: self.selecionar_escolha("Pedra")) # Cria o botão de escolha de pedra
        botao_papel = tk.Button(self, text="Papel", command=lambda: self.selecionar_escolha("Papel")) # Cria o botão de escolha de papel
        botao_tesoura = tk.Button(self, text="Tesoura", command=lambda: self.selecionar_escolha("Tesoura")) # Cria o botão de escolha de tesoura

        botao_pedra.pack() # Adiciona o botão de escolha pedra
        botao_papel.pack() # Adiciona o botão de escolha pedra
        botao_tesoura.pack() # Adiciona o botão de escolha pedra

        self.protocol("WM_DELETE_WINDOW", self.fechar_janela) # Cria um protocolo

    def selecionar_escolha(self, escolha): # Cria a função para definir a escolha
        self.escolha_do_usuario = escolha # Define a escolha
        self.destroy() # Fecha a janela

    def fechar_janela(self): # Cria uma função para fechar a janela
        self.escolha_do_usuario = None # Define a escolha do jogador como nenhuma
        self.destroy() # Fecha a janela
    
# Cria a função para obter o vencedor
def determinar_vencedor(escolha_usuario0, escolha_usuario1, nome_usuario0, nome_usario1):
    if escolha_usuario0 == escolha_usuario1: # Se as escolhas fdorem iguais determina que é um empate
        return "Empate" # Retorna falando que foi um empate
    # Confere todos cenários possiveis de vitória
    elif (escolha_usuario0 == "Pedra" and escolha_usuario1 == "Tesoura") or \
         (escolha_usuario0 == "Papel" and escolha_usuario1 == "Pedra") or \
         (escolha_usuario0 == "Tesoura" and escolha_usuario1 == "Papel"):
        return f"O jogador {nome_usuario0} ganhou!" # Retorna que o user 2 ganhou
    else: # Se o user 0 não ganhar o user 1 ganha
        
        return f"O jogador {nome_usario1} ganhou!" # Retorna que o user 1 ganhou

quer_jogar = input("Vocês querem jogar uma partida? (Sim para jogar) ") # Pergunta se querem jogar inicialmente

if (quer_jogar.lower() == "sim"): # Se quiserem jogar o programa roda
    nome0 = input("Qual o seu nome? ") # Pergunta o nome do primeiro jogador
    nome1 = input("Qual o seu nome? ") # Pergunta o nome do segundo jogador
    vitorias.update({nome0 : 0, nome1 : 0})
    
    while quer_jogar.lower() == "sim":
        escolha_do_usuario = None # Seta a escolha como nenhuma

        print(f"Escolha do jogador {nome0}") # Fala de quem é a vez de escolher
        janela_jogador0 = EscolhaJanela(nome0) # Cria a janela
        janela_jogador0.mainloop() # Abre a janela
        escolha_jogador0 = janela_jogador0.escolha_do_usuario # Define a escolha do usuario

        print(f"Escolha do jogador {nome1}") # Fala de quem é a vez de escolher
        janela_jogador1 = EscolhaJanela(nome1) # Cria a janela
        janela_jogador1.mainloop() # Abre a janela
        escolha_jogador1 = janela_jogador1.escolha_do_usuario # Define a escolha do usuario

        jogador0 = Jogador(nome0, escolha_jogador0) # Seta o jogador
        jogador1 = Jogador(nome1, escolha_jogador1) # Seta o jogador

        print(determinar_vencedor(jogador0.escolha, jogador1.escolha, jogador0.nome, jogador1.nome)) # Puxa a função para ver o vencedor
        
        if nome0 in determinar_vencedor(jogador0.escolha, jogador1.escolha, jogador0.nome, jogador1.nome): # Confere se o primeiro jogador ganhou
            vitorias[nome0] += 1 # Adiciona uma vitória para ele
        elif nome1 in determinar_vencedor(jogador0.escolha, jogador1.escolha, jogador0.nome, jogador1.nome): # Confere se o segundo jogador ganhou
            vitorias[nome1] += 1 # Adiciona uma vitória para ele

        quer_jogar = input("Vocês querem jogar mais uma partida? (Sim para jogar) ") # Pergunta se querem jogar novamente

for jogador, vitoria in vitorias.items(): # Cria um looping para pegar todos os valores e enviar formatado
    print(f"{jogador}: {vitoria} vitórias") # Envia formatado
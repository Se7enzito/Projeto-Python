import tkinter as tk

class Time():
    def __init__(self, nome, cidade, mascote):
        self._nome = nome
        self._cidade = cidade
        self._mascote = mascote

    @property
    def nota(self):
        return self._nome
    
    @property
    def peso(self):
        return self._cidade
    
    @property
    def mascote(self):
        return self._mascote

class Jogador():
    def __init__(self, nome, time, camisa):
        self._nome = nome
        self._time = time
        self._camisa = camisa

    @property
    def nome(self):
        return self._nome
    
    @property
    def time(self):
        return self._time
    
    @property
    def camisa(self):
        return self._camisa
    
class CommisaoTec():
    def __init__(self, tec, aux, prep):
        self._tec = tec
        self._aux = aux
        self._prep = prep

    @property
    def tec(self):
        return self._tec
    
    @property
    def aux(self):
        return self._aux
    
    @property
    def prep(self):
        return self._prep
    
class Tecnico():
    def __init__(self, nome, time, esquema):
        self._nome = nome
        self._time = time
        self._esquema = esquema

    @property
    def nome(self):
        return self._nome
    
    @property
    def time(self):
        return self._time
    
    @property
    def esquema(self):
        return self._esquema
    
class Auxiliar():
    def __init__(self, nome, time, esquema):
        self._nome = nome
        self._time = time
        self._esquema = esquema
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def time(self):
        return self._time
    
    @property
    def esquema(self):
        return self._esquema

    def esta_coletiva(self):
        dar_coletiva = "O auxiliar técnico está dando uma coletiva de impresa."
        return dar_coletiva
    
class Preparador():
    def __init__(self, nome, time, elenco):
        self._nome = nome
        self._time = time
        self._elenco = elenco
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def time(self):
        return self._time
    
    @property
    def elenco(self):
        return self._elenco

    def esta_coletiva(self):
        dar_coletiva = "O preparador físico está dando uma coletiva de imprensa."
        return dar_coletiva

class EscolhaJanela(tk.Tk):
    def __init__(self): # Falando que tem o nome do jogador na janela
        super().__init__() # Inicia o __init__
        self.title("") # Cria o nome da janela
        self.escolha_do_usuario = None # Seta escolha do jogador como nenhuma

        botao_jogador = tk.Button(self, text="Jogador", command=lambda: self.selecionar_escolha("jogador")) # Cria o botão de escolha de registrar jogador
        botao_time = tk.Button(self, text="Time", command=lambda: self.selecionar_escolha("time")) # Cria o botão de escolha de registrar time
        botao_comtec = tk.Button(self, text="Comissão Técnica", command=lambda: self.selecionar_escolha("comissaotec")) # Cria o botão de escolha de registrar comissão técnica

        botao_jogador.pack() # Adiciona o botão de escolha jogador
        botao_time.pack() # Adiciona o botão de escolha time
        botao_comtec.pack() # Adiciona o botão de escolha comissão técnica

        self.protocol("WM_DELETE_WINDOW", self.fechar_janela) # Cria um protocolo

    def selecionar_escolha(self, escolha): # Cria a função para definir a escolha
        self.escolha_do_usuario = escolha # Define a escolha
        self.destroy() # Fecha a janela

    def fechar_janela(self): # Cria uma função para fechar a janela
        self.escolha_do_usuario = None # Define a escolha do jogador como nenhuma
        self.destroy() # Fecha a janela

quer_cadastrar = "" # Cria uma condição para o looping
lista_jogadores = [] # Lista dos jogadores
lista_times = [] # Lista dos times
lista_comissaotecs = [] # Lista das comissões técnicas
lista_tecs = [] # Lista de técnicos
lista_auxs = [] # Lista de auxiliares
lista_preps = [] # Lista de preparadores

def cadastrar_jogador():
    nome = input("Qual o nome do jogador? ") # Pede o nome do jogador
    time = input("Qual o time do jogador? ") # Pede o time do jogador
    camisa = int(input("Qual a camisa do jogador? ")) # Pede a camisa do jogador

    jogador = Jogador(nome, time, camisa) # Registra o jogador
    lista_jogadores.append(jogador) # Registra o jogador dentro da lista
        

def cadastrar_time():
    nome = input("Qual o nome do time? ") # Pede o nome do jogador
    cidade = input("Qual a cidade para jogos mandantes? ") # Pede o time do jogador
    mascote = int(input("Qual o nome do mascote do time? ")) # Pede a camisa do jogador

    time = Time(nome, cidade, mascote) # Cadastra o jogador
    lista_times.append(time)

def cadastrar_comissaotec():
    time = input("Qual o nome do time? ") # Pede o nome do time
    tec_nome = input("Qual o nome do técnico? ") # Pede o nome do técnico
    aux_nome = input("Qual o nome do auxiliar? ") # Pede o nome do auxiliar
    prep_nome = int(input("Qual o nome do preparador? ")) # Pede o nome do preparador
    tec_esquema = input(" ") # Pede o esquema preferido
    aux_esquema = input(" ") # Pede o esquema preferido
    prep_elenco = input(" ") # Pede parte do elenco que cuida

    tec = Tecnico(tec_nome, time, tec_esquema) # Cadastra o técnico
    lista_tecs.append(tec) # Registra o técnico dentro da lista
    aux = Auxiliar(aux_nome, time, aux_esquema) # Cadastra o auxiliar
    lista_auxs.append(aux) # Registra o auxiliar dentro da lista
    prep = Preparador(prep_nome, time, prep_elenco) # Cadastra o preparador
    lista_preps.append(prep) # Registra o preparador dentro da lista
    comtec = CommisaoTec(tec, aux, prep) # Cadastra a comissão técnica
    lista_comissaotecs.append(comtec) # Registra a comissão técnica dentro da lista

def exibir_jogadores():
    print("Lista de jogadores:\n")

    for jogador in lista_jogadores:
        print(f"Nome: {jogador.nome} Time: {jogador.time}, Camisa: {jogador.camisa}\n")

while quer_cadastrar.lower() != "não": # Pergunta se quer cadastrar algo
    print(f"Selecione o que você quer cadastrar") # Mensagem falando para selecionar o que quer cadastrar
    janela_cadastro = EscolhaJanela() # Cria janela de cadastro
    janela_cadastro.mainloop() # Abre a janela
    tipo_cadastro = janela_cadastro.escolha_do_usuario # Define a escolha de tipo do cadastro

    if (tipo_cadastro == "jogador"): # Confere se escolheu jogador
        cadastrar_jogador() # Chama a função de cadastro
    elif (tipo_cadastro == "time"): # Confere se escolheu time
        cadastrar_time() # Chama a função de cadastro
    elif (tipo_cadastro == "comissaotec"): # Confere se escolheu comissaotec
        cadastrar_comissaotec() # Chama a função de cadastro
    else: # Caso não seja nada
        print("Não encontrado este tipo de escolha.") # Envia mensagem de erro

    quer_cadastrar = input("Você quer cadastrar mais jogadores? ('Sim' para cadastrar ou 'Não' para parar) ") # Pergunta se ainda quer cadastrar algum jogador

exibir_jogadores()
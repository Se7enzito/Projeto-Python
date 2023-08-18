class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    
    def comer(self):
        print(f"O {self.nome} está comendo.")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

cachorro = Cachorro("Toto", "Preto")
gato = Gato("Bichano", "Branco")

gato.comer()
cachorro.comer()
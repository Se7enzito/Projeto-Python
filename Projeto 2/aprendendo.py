class Carro():
    def __init__(self, marca, modelo, ano, peso, possui_4_portas) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.peso = peso
        self.possui_4_portas = possui_4_portas
    
    def ligar(self):
        return print(f'O {self.modelo}. Esta ligado')
    
celtinha = Carro('Chevrolet', 'Celta', '2009', 1200, False)

print(celtinha.modelo)
celtinha.ligar()
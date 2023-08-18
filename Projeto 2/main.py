class Aluno():
    def __init__(self, nome, id, serie):
        self.nome = nome
        self.id = id
        self.serie = serie
        self._nota = 0
        self._peso = 0

    @property
    def nota(self):
        return self._nota
    
    @property
    def peso(self):
        return self._peso
    
    def registrar_peso(self, peso):
        self._peso = peso

    def registrar_nota(self, nota):
        self._nota = nota
    
a1 = Aluno('Bernardo', 1, '2° Ano')
a2 = Aluno('Laura', 2, '3° Ano')

print(f"Aluno: {a1.nome}\nID: {a1.id}\nAno: {a1.serie}\nNota: {a1.nota}\nPeso: {a1.peso}\n")
print(f"Aluno: {a2.nome}\nID: {a2.id}\nAno: {a2.serie}\nNota: {a2.nota}\nPeso: {a2.peso}\n")

print("Atualizando...")
a1.registrar_nota(10)
a1.registrar_peso(2)

a2.registrar_nota(30)
a2.registrar_peso(5)
print("Tabela atualizada:\n")

print(f"Aluno: {a1.nome}\nID: {a1.id}\nAno: {a1.serie}\nNota: {a1.nota}\nPeso: {a1.peso}\n")
print(f"Aluno: {a2.nome}\nID: {a2.id}\nAno: {a2.serie}\nNota: {a2.nota}\nPeso: {a2.peso}\n")
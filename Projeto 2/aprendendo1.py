class Funcionario():
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self._salario = 0
        self._hora_trabalhada = 0

    @property
    def salario(self):
        return self._salario
    
    @property
    def hora_trabalhada(self):
        return self._hora_trabalhada
    
    @salario.setter
    def salario(self, novo_salario):
        raise ValueError("Impossivel alterar o salario diretamente. Use a funcao calcula_salario()")
    
    def registrar_hora_trabalhada(self):
        self._hora_trabalhada += 1
    
    def calcula_salario(self):
        self._salario = self._hora_trabalhada * self.valor_hora_trabalhada

fun1 = Funcionario("Bernardo", "Programador", 400)

print(f"Salario atual: {fun1.salario}")
print(f"Valor por hora: {fun1.valor_hora_trabalhada}")

for _ in range(5):
    fun1.registrar_hora_trabalhada()

print(f"Horas trabalhadas: {fun1.hora_trabalhada}")

fun1.calcula_salario()

print(f"Novo salario: {fun1.salario}")
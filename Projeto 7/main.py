from conexao import Conexao as Conn

nova_conexao = Conn("Projeto 7/database.db", "", "")

# V1.0

# condicao = 0

# while condicao == 0:
#     nome = str(input("Qual o nome completo do aluno? "))
#     first = str(input("Qual o primeiro nome do aluno? "))
#     last = str(input("Qual o último nome do aluno? "))

#     cadastro = nova_conexao.inserir_dado(first, last, nome)

#     print(f"Aluno cadastrado: {cadastro}")

#     dados = nova_conexao.consultar_tabela()

#     for dado in dados:
#         print(dado[0])
#         print(dado[1])
#         print(dado[2])
#         print(dado[3])

#     condicao = int(input("Você deseja sair do cadastrador? (0 - Não; 1 - Sim) "))

# V2.0

condicao = int(input("Você deseja sair do cadastrador? (0 - Sim; 1 - Cadastrar; 2 - Ver lista de alunos; 3 - Consultar aluno; 4 - Atualizar dados) "))

while condicao != 0:

    if condicao == 1:
        nome = str(input("Qual o nome completo do aluno? "))
        first = str(input("Qual o primeiro nome do aluno? "))
        last = str(input("Qual o último nome do aluno? "))
        idade = int(input("Qual a idade do aluno? "))

        cadastro = nova_conexao.inserir_dado(first, last, nome, idade)

        print(f"Aluno cadastrado: {cadastro}")
    elif condicao == 2:
        dados = nova_conexao.consultar_tabela()

        for dado in dados:
            print(f"ID: {dado[0]}")
            print(f"Primeiro nome: {dado[1]}")
            print(f"Último nome: {dado[2]}")
            print(f"Nome completo: {dado[3]}")
            print(f"Idade: {dado[4]}")

    elif condicao == 3:
        id = int(input("Qual o ID do aluno? "))

        dados = nova_conexao.consultar_dado(id)

        for dado in dados:
            print(f"ID: {dado[0]}")
            print(f"Primeiro nome: {dado[1]}")
            print(f"Último nome: {dado[2]}")
            print(f"Nome completo: {dado[3]}")
            print(f"Idade: {dado[4]}")

    condicao = int(input("Você deseja sair do cadastrador? (0 - Sim; 1 - Cadastrar; 2 - Ver lista de alunos; 3 - Consultar aluno) "))
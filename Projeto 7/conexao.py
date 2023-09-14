import sqlite3 as sql

class Conexao:
    def __init__(self, database: str, username: str, password: str) -> None:
        self.database = database
        self.username = username
        self.password = password
        self.connection = None
        self.cursor = None

    # def login(self) -> bool:
    #     return True if self.username == "admin" and "1234" == self.password else False

    def conectar(self) -> bool:
        self.connection = sql.connect(self.database)
        self.cursor = self.connection.cursor()
        return True

    def desconectar(self) -> bool:
        self.connection.close()

    def inserir_dado(self, first_name: str, last_name: str, full_name: str, idade: int, telefone: int, media: int) -> None:
        self.conectar()
        self.cursor.execute("INSERT INTO users (first_name, last_name, full_name, idade, telefone, media) VALUES (?, ?, ?, ?, ?, ?)", (first_name, last_name, full_name, idade, telefone, media))
        self.connection.commit()
        self.desconectar()

        return (first_name, last_name, full_name, idade, telefone, media)

    # def atualizar_dado(self, id: int, **valores: dict) -> None:
    #     self.conectar()
    #     self.cursor.execute("UPDATE users (first_name, last_name, full_name, idade) WHERE id = ? VALUES (?, ?, ?)", (id, valores['first_name'], valores['last_name'], valores['full_name'], valores['idade']))
    #     self.connection.commit()
    #     self.desconectar()

    #     return valores

    def apagar_dado(self, id: int) -> None:
        self.conectar()
        backup = self.consultar_dado(id)
        self.cursor.execute("DELETE * FROM users WHERE id = ?", (id,))
        self.connection.commit()
        self.desconectar()

        return backup

    def consultar_dado(self, id: int) -> list:
        self.conectar()
        consulta = self.cursor.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchall()
        self.desconectar()

        return consulta

    def limpar_tabela(self) -> None:
        self.conectar()
        self.cursor.execute("DELETE * FROM users")
        self.connection.commit()
        self.desconectar()


    def consultar_tabela(self) -> None:
        self.conectar()
        consulta = self.cursor.execute("SELECT * FROM users").fetchall()
        self.desconectar()

        return consulta


if __name__ == "__main__":
    pass
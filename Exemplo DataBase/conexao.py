import sqlite3 as sql

class Conexao:
    def __init__(self, database: str, username: str, password: str) -> None:
        self.database = database
        self.username = username
        self.password = password
        self.connection = None
        self.cursor     = None


    def login(self) -> bool:
        """
        Este método valida as credenciais do usuário.

        Parâmetros:
            None

        Return:
            bool
        """
        return True if self.username == "admin" and "1234" == self.password else False


    def conectar(self) -> bool:
        if self.login():
            self.connection = sql.connect(self.database)
            self.cursor     = self.connection.cursor()
            return True


    def desconectar(self) -> bool:
        self.connection.close()


    def inserir_dado(self, nickname: str, first_name: str, last_name: str, score: float) -> None:
        self.conectar()
        self.cursor.execute("INSERT INTO users (nickname, first_name, last_name, score) VALUES (?, ?, ?, ?)", (nickname, first_name, last_name, score))
        self.connection.commit()
        self.desconectar()

        return (nickname, first_name, last_name, score)


    def inserir_kwdado(self, **valores: dict) -> dict:
        self.conectar()
        self.cursor.execute("INSERT INTO users (nickname, first_name, last_name, score) VALUES (?, ?, ?, ?)", (valores['nickname'], valores['first_name'], valores['last_name'], valores['score']))
        self.connection.commit()
        self.desconectar()

        return valores


    def atualizar_dado(self, id: int, **valores: dict) -> None:
        self.conectar()
        self.cursor.execute("UPDATE users (nickname, first_name, last_name, score) WHERE id = ? VALUES (?, ?, ?, ?)", (id, valores['nickname'], valores['first_name'], valores['last_name'], valores['score']))
        self.connection.commit()
        self.desconectar()

        return valores


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
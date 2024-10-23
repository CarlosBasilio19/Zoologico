import mysql.connector

class Animal:

    def __init__(self, nome, cor, habitat,idade):
        self.nome = nome
        self.cor = cor
        self.habitat = habitat
        self.idade = idade

    def fazer_som(self):
        print("O animal faz um som.")

    def informacoes(self):
        print(f"{self.nome} é {self.cor}, seu habitat é {self.habitat} e tem {self.idade} anos de idade.")


    def salvar_no_banco(self):
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="6363",
                database="zoologico"
            )
            cursor = conexao.cursor()

            # Query para inserir os dados do animal no banco de dados
            sql = "INSERT INTO animais (nome, cor, habitat, idade) VALUES (%s, %s, %s, %s)"
            valores = (self.nome, self.cor, self.habitat, self.idade)

            cursor.execute(sql, valores)
            conexao.commit()

            print(f"{self.nome} foi salvo no banco de dados.")

        except mysql.connector.Error as err:
            print(f"Erro: {err}")

        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()


    @staticmethod
    def listar_animais():
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="6363",
                database="zoologico"
            )
            cursor = conexao.cursor()


            cursor.execute("SELECT * FROM animais")
            animais = cursor.fetchall()

            for animal in animais:
                print(f"ID: {animal[0]}, Nome: {animal[1]}, Cor: {animal[2]}, Habitat: {animal[3]}, Idade: {animal[4]}")

        except mysql.connector.Error as err:
            print(f"Erro: {err}")

        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()




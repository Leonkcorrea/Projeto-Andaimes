import sqlite3

connection = sqlite3.connect('databaseClientes.db')
c = connection.cursor()

def ADD(nome, endereco, bairro, cep, cidade, estado, contato, cpf, rg, pessoa):
    c.execute("""INSERT INTO CLIENTE VALUES(:nome, :endereco, :bairro, :cep, :cidade, :estado, :contato, :cpf, :rg, :pessoa)""",
         {'nome': nome, 'endereco': endereco, 'bairro':bairro, 'cep':cep, 'cidade':cidade, 'estado':estado, 'contato':contato, 'cpf':cpf, 'rg':rg, 'pessoa':pessoa})
    c.execute("SELECT * FROM CLIENTE")
    # print(c.fetchall())
    # connection.commit()
    connection.close()

nome = ""
endereco = ""
bairro = ""
cep = ""
cidade = ""
estado = ""
contato = ""
cpf = ""
rg = ""
pessoa = ""

ADD(nome, endereco, bairro, cep, cidade, estado, contato, cpf, rg, pessoa)
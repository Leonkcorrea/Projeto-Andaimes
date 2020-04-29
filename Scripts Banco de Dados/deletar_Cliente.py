import sqlite3

connection = sqlite3.connect('databaseClientes.db')
c = connection.cursor()

def DELETE(cpf):
    c.execute("DELETE FROM CLIENTE WHERE cpf=:cpf", {'cpf': cpf})
    c.execute("SELECT * FROM CLIENTE")
    print(c.fetchall())
    connection.commit()
    connection.close()

cpf = ""

DELETE(cpf)
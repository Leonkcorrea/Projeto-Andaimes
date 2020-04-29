import sqlite3

connection = sqlite3.connect('databasePeças.db')
c = connection.cursor()

def ADD(codigo, nomeSingular, nomePlural, genero, preco):
    c.execute("""INSERT INTO PECA VALUES(:codigo, :nomeSingular, :nomePlural, :genero, :preco)""",
         {'codigo': codigo, 'nomeSingular': nomeSingular, 'nomePlural':nomePlural, 'genero':genero, 'preco':preco})
    c.execute("SELECT * FROM PECA")
    print(c.fetchall())
    connection.commit()
    connection.close()

codigo = ".abc"
nomeSingular = "nome"
nomePlural = "nomes"
genero = "M"
preco = "2.50"

ADD(codigo, nomeSingular, nomePlural, genero, preco)
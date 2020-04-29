import sqlite3

connection = sqlite3.connect('databasePeças.db')
c = connection.cursor()

def DELETE(codigo):
    c.execute("DELETE FROM PECA WHERE codigo=:codigo", {'codigo': codigo})
    c.execute("SELECT * FROM PECA")
    print(c.fetchall())
    connection.commit()
    connection.close()

codigo = ".abc"

DELETE(codigo)
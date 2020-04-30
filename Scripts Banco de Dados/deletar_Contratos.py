import sqlite3

connection = sqlite3.connect('databaseContratos.db')
c = connection.cursor()

def DELETE(codigo):
    c.execute("DELETE FROM CONTRATO WHERE codigo=:codigo", {'codigo': codigo})
    c.execute("SELECT * FROM CONTRATO")
    print(c.fetchall())
    connection.commit()
    connection.close()

codigo = "a"

DELETE(codigo)
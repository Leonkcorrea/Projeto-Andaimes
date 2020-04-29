import sqlite3

connection = sqlite3.connect('databasePeças.db')
c = connection.cursor()

def CREATE():
    # PEÇA #
    c.execute('CREATE TABLE IF NOT EXISTS PECA (\
        `codigo` VARCHAR(5) NOT NULL,\
        `nomeSingular` VARCHAR(25) NOT NULL,\
        `nomePlural` VARCHAR(25) NOT NULL,\
        `genero` VARCHAR(1) NOT NULL,\
        `preco` VARCHAR(8),\
        PRIMARY KEY(`codigo`));')
    connection.commit()
    connection.close()  
CREATE()
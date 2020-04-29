import sqlite3

connection = sqlite3.connect('databaseClientes.db')
c = connection.cursor()

def CREATE():
    # CLIENTE #
    c.execute("""CREATE TABLE IF NOT EXISTS CLIENTE (
        `nome` VARCHAR (60) NOT NULL,
        `endereco` VARCHAR (50),
        `bairro` VARCHAR(20),
        `cep` VARCHAR(9),
        `cidade` VARCHAR(20),
        `estado` VARCHAR(2),
        `contato` VARCHAR(30),
        `cpf` VARCHAR(14) NOT NULL,
        `rg` VARCHAR(14),
        `pessoa` VARCHAR(1));""")
    connection.commit()
    connection.close()
CREATE()
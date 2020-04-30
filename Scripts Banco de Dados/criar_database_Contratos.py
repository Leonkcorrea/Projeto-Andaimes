import sqlite3

connection = sqlite3.connect('databaseContratos.db')
c = connection.cursor()

def CREATE():
    # CONTRATO # 
    c.execute("""CREATE TABLE IF NOT EXISTS CONTRATO (
        `codigo` VARCHAR(6) NOT NULL,
        `tipo` VARCHAR(1),
        `pessoa` VARCHAR(1),
        `numero` VARCHAR(4) NOT NULL,
        `ano` VARCHAR(2),
        `nome` VARCHAR(50),
        `endereco` VARCHAR(20),
        `bairro` VARCHAR(20),
        `cep` VARCHAR(9),
        `cidade` VARCHAR(20),
        `estado` VARCHAR(2),
        `contato` VARCHAR(30),
        `text` VARCHAR(1),
        `texto` VARCHAR(40),
        `dataInicio` VARCHAR(10),
        `data` VARCHAR(10),
        `vlr` VARCHAR(8),
        `valor` VARCHAR(40),
        `dataHoje` VARCHAR(10),
        `cpf` VARCHAR(15),
        `rg` VARCHAR(15),
        
        `prod1` VARCHAR(5), `qtd1` INT,
        `prod2` VARCHAR(5), `qtd2` INT,
        `prod3` VARCHAR(5), `qtd3` INT,
        `prod4` VARCHAR(5), `qtd4` INT,
        `prod5` VARCHAR(5), `qtd5` INT,
        `prod6` VARCHAR(5), `qtd6` INT,
        `prod7` VARCHAR(5), `qtd7` INT)""")
    connection.commit()
    connection.close()
CREATE()
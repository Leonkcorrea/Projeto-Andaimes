import sqlite3

connection = sqlite3.connect('databasePagamentos.db')
c = connection.cursor()

def CREATE():
    # PAGAMENTOS # 
    c.execute("""CREATE TABLE IF NOT EXISTS PAGAMENTOS (
        `id_pagamento` INT NOT NULL,
        `nome` VARCHAR(50),
        `codigo_contrato` VARCHAR(6),
        `obs` VARCHAR(1),
        `nf` VARCHAR(4),
        `data_pagamento` VARCHAR(10),
        `forma_pagamento` VARCHAR(1),
        `data_vencimento` VARCHAR(10),
        `valor` VARCHAR(7))""")
    connection.commit()
    connection.close()
CREATE()
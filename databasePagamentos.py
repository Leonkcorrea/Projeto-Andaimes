import sqlite3

connection = sqlite3.connect('databasePagamentos.db')
c = connection.cursor()

def CREATE():
    # PAGAMENTOS # 
    c.execute('CREATE TABLE IF NOT EXISTS PAGAMENTOS (\
        `id_pagamento` INT NOT NULL,\
        `data_pagamento` DATE,\
        `forma_pagamento` INT,\
        `data_vencimento` DATE\
        PRIMARY KEY(`id_pagamento`))')
    connection.commit()
CREATE()
import sqlite3

connection = sqlite3.connect('databasePagamentos.db')
c = connection.cursor()

def ADD(id_pagamento, nome, codigo_documento, obs, nf, data_pagamento, forma_pagamento, data_vencimento, valor):
    c.execute("""INSERT INTO PAGAMENTOS VALUES(:id_pagamento, :nome, :codigo_documento, :obs, :nf, :data_pagamento, :forma_pagamento, :data_vencimento, :valor)""",
         {'id_pagamento': id_pagamento, 'nome': nome, 'codigo_documento':codigo_documento, 'obs':obs, 'nf':nf, 'data_pagamento':data_pagamento, 'forma_pagamento':forma_pagamento, 'data_vencimento':data_vencimento, 'valor':valor})
    c.execute("SELECT * FROM PAGAMENTOS")
    print(c.fetchall())
    connection.commit()
    connection.close()

id_pagamento = ''
nome = ''
codigo_documento = ''
obs = ''
nf = ''
data_pagamento = ''
forma_pagamento = ''
data_vencimento = ''
valor = ''

ADD(id_pagamento, nome, codigo_documento, obs, nf, data_pagamento, forma_pagamento, data_vencimento, valor)
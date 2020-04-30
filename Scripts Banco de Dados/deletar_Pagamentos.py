import sqlite3

connection = sqlite3.connect('databasePagamentos.db')
c = connection.cursor()

def DELETE(id_pagamento):
    c.execute("DELETE FROM PAGAMENTOS WHERE id_pagamento=:id_pagamento", {'id_pagamento': id_pagamento})
    c.execute("SELECT * FROM PAGAMENTOS")
    print(c.fetchall())
    connection.commit()
    connection.close()

id_pagamento = ""

DELETE(id_pagamento)
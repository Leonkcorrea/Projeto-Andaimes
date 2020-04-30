import sqlite3

connection = sqlite3.connect('databaseContratos.db')
c = connection.cursor()

def ADD(codigo, tipo, pessoa, numero, ano, nome, endereco, bairro, cep, cidade, estado, contato, text, texto, dataInicio, data,
 vlr, valor, dataHoje, cpf, rg, prod1, qtd1, prod2, qtd2, prod3, qtd3, prod4, qtd4, prod5, qtd5, prod6, qtd6, prod7, qtd7):
    c.execute("""INSERT INTO CONTRATO VALUES(:codigo, :tipo, :pessoa, :numero, :ano, :nome, :endereco, :bairro, :cep, :cidade, 
        :estado, :contato, :text, :texto, :dataInicio, :data, :vlr, :valor, :dataHoje, :cpf, :rg, :prod1, 
        :qtd1, :prod2, :qtd2, :prod3, :qtd3, :prod4, :qtd4, :prod5, :qtd5, :prod6, :qtd6, :prod7, :qtd7)""", {'codigo': codigo,
         'tipo': tipo, 'pessoa':pessoa, 'numero':numero, 'ano':ano, 'nome':nome, 'endereco':endereco,'bairro':bairro,
          'cep':cep, 'cidade':cidade, 'estado':estado, 'contato':contato, 'text':text, 'texto':texto, 'dataInicio':dataInicio,
          'data':data, 'vlr':vlr, 'valor':valor, 'dataHoje':dataHoje, 'cpf':cpf, 'rg':rg,'prod1':prod1, 'qtd1':qtd1,
          'prod2':prod2, 'qtd2':qtd2, 'prod3':prod3, 'qtd3':qtd3, 'prod4':prod4, 'qtd4':qtd4,
          'prod5':prod5, 'qtd5':qtd5, 'prod6':prod6, 'qtd6':qtd6, 'prod7':prod7, 'qtd7':qtd7})
    c.execute("SELECT * FROM CONTRATO")
    print(c.fetchall())
    connection.commit()
    connection.close()

codigo = 'a'
tipo = 'a'
pessoa = 'a'
numero = 'a'
ano = 'a'
nome = 'a'
endereco = 'a'
bairro = 'a'
cep = 'a'
cidade = 'a'
estado = 'a'
contato = 'a'
text = 'a'
texto = 'a'
dataInicio = 'a'
data = 'a'
vlr = 'a'
valor = 'a'
dataHoje = 'a'
cpf = 'a'
rg = 'a'
prod1 = 'a'
qtd1 = 1
prod2 = 'a'
qtd2 = 1
prod3 = 'a'
qtd3 = 1
prod4 = 'a'
qtd4 = 1
prod5 = 'a'
qtd5 = 1
prod6 = 'a'
qtd6 = 1
prod7 = 'a'
qtd7 = 1

ADD(codigo, tipo, pessoa, numero, ano, nome, endereco, bairro, cep, cidade, estado, contato, text, texto, dataInicio, data,
 vlr, valor, dataHoje, cpf, rg, prod1, qtd1, prod2, qtd2, prod3, qtd3, prod4, qtd4, prod5, qtd5, prod6, qtd6, prod7, qtd7)
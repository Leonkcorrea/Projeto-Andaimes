import openpyxl
from openpyxl import Workbook
import sqlite3

connection = sqlite3.connect('databaseContatos.db')
c = connection.cursor()

def NOME():
    return 'retornar nome do contrato do banco de dados'

def ENDERECO():
    return 'retornar endereço do contrato do banco de dados'

def CIDADE():
    return 'retornar cidade do contrato do banco de dados'

def ESTADO():
    return 'retornar estado do contrato do banco de dados'

def CEP():
    return 'retornar cep do contrato do banco de dados'

def OUTROS():
    return 'retornar OUTROS do contrato do banco de dados'


def GERAR_COBRANÇA():
    documento = Workbook()

    planilha = documento.active
    planilha.title = "Cobrança"

    planilha['B10'] = '<valor>'
    planilha['B14'] = '<nome>'
    planilha['B16'] = '<endereço>' + ' - ' + '<bairro>'
    planilha['B18'] = '<cidade>'
    planilha['B20'] = '<rg/ie>'

    planilha['C23'] = '<valorExtenso>'

    planilha['G10'] = '<data>'
    planilha['G14'] = '<data2>'
    planilha['G18'] = '<estado>'

    planilha['I18'] = '<cpf/cnpj>'

    documento.save("TEMPLATE_COBRANÇA_PYTHON.xlsx")

GERAR_COBRANÇA()
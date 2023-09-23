
from sqlalchemy import create_engine
import os
import os
from ftplib import FTP
import mysql.connector


#Download the file with guidance on fact table columns


dir = 'D:\\Projetos\\Projetos\\Brazilian_Census'
list_files = os.listdir(dir)
filename = 'populacao.pdf'


try:

    for files in list_files:
        if files == filename:
            print('Already Downloaded')

        else:
            ftp = FTP("ftp.datasus.gov.br")
            ftp.login() 

            ftp.cwd("/dissemin/publicos/IBGE/doc/")  

            guidance_table = 'populacao.pdf'


            with open(guidance_table, 'wb') as arquivo:
                ftp.retrbinary('RETR ' + guidance_table, arquivo.write)

except Exception as e:
    print(e)


#DB Connection

db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='112233',
    database='projeto1'
)

# Cursor SQL
cursor = db_connection.cursor()




#Building the dim_tables

tabela_sexo = {
    1: 'Masculino',
    2: 'Feminino'
}

criar_tabela_sexo = """
CREATE TABLE IF NOT EXISTS sexo_tabela (
    sexo_id INT PRIMARY KEY,
    sexo VARCHAR(20)
)
"""

criar_tabela_fxetaria = """
CREATE TABLE IF NOT EXISTS fxetaria (
    fxetaria_id INT PRIMARY KEY,
    fxetaria VARCHAR(20)
)
"""

cursor.execute(criar_tabela_sexo)



criar_tabela_situacao = """
CREATE TABLE IF NOT EXISTS situacao (
    situacao_id INT PRIMARY KEY,
    situacao VARCHAR(20)
)
"""

cursor.execute(criar_tabela_situacao)

cursor.execute(criar_tabela_fxetaria)






# Dados para inserção

dados_sexo = [
    (1, 'Masculino'),
    (2, 'Feminino')
]

dados_situacao = [
    (1,'Urbano'),
    (2, 'Rural'),
    (3, 'Não Levantado')
    ] 

dados_fxetaria = [
    ('0', 'menor de 1 ano'),
    ('101', '1 ano'),
    ('202', '2 anos'),
    ('303', '3 anos'),
    ('404', '4 anos'),
    ('505', '5 anos'),
    ('606', '6 anos'),
    ('707', '7 anos'),
    ('808', '8 anos'),
    ('909', '9 anos'),
    ('1010', '10 anos'),
    ('1111', '11 anos'),
    ('1212', '12 anos'),
    ('1313', '13 anos'),
    ('1414', '14 anos'),
    ('1515', '15 anos'),
    ('1616', '16 anos'),
    ('1717', '17 anos'),
    ('1818', '18 anos'),
    ('1919', '19 anos'),
    ('2024', '20 a 24 anos'),
    ('2529', '25 a 29 anos'),
    ('3034', '30 a 34 anos'),
    ('3539', '35 a 39 anos'),
    ('4044', '40 a 44 anos'),
    ('4549', '45 a 49 anos'),
    ('5054', '50 a 54 anos'),
    ('5559', '55 a 59 anos'),
    ('6064', '60 a 64 anos'),
    ('6569', '65 a 69 anos'),
    ('7074', '70 a 74 anos'),
    ('7579', '75 a 79 anos'),
    ('8099', '80 anos e mais'),
    ('1000', 'idade ignorada')
]


# Inserção dos valores

inserir_dados_sexo = "INSERT INTO sexo_tabela (sexo_id, sexo) VALUES (%s, %s)"
cursor.executemany(inserir_dados_sexo, dados_sexo)

inserir_dados_situacao = "INSERT INTO situacao (situacao_id, situacao) VALUES (%s, %s)"
cursor.executemany(inserir_dados_situacao, dados_situacao)

inserir_dados_fxetaria = "INSERT INTO fxetaria (fxetaria_id, fxetaria) VALUES (%s, %s)"
cursor.executemany(inserir_dados_fxetaria, dados_fxetaria)


# Commit das alterações
db_connection.commit()

# Fechar conexão
cursor.close()
db_connection.close()









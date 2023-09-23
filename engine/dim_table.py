import pandas as pd
from sqlalchemy import create_engine
import os
import wget
import os
import zipfile
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

cursor.execute(criar_tabela_sexo)



criar_tabela_situacao = """
CREATE TABLE IF NOT EXISTS situacao (
    situacao_id INT PRIMARY KEY,
    situacao VARCHAR(20)
)
"""

cursor.execute(criar_tabela_situacao)






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


# Inserção dos valores

inserir_dados_sexo = "INSERT INTO sexo_tabela (sexo_id, sexo) VALUES (%s, %s)"
cursor.executemany(inserir_dados_sexo, dados_sexo)

inserir_dados_situacao = "INSERT INTO situacao (situacao_id, situacao) VALUES (%s, %s)"
cursor.executemany(inserir_dados_situacao, dados_situacao)

# Commit das alterações
db_connection.commit()

# Fechar conexão
cursor.close()
db_connection.close()







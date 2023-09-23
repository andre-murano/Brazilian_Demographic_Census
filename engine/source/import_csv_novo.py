import pandas as pd
from sqlalchemy import create_engine
import os

# from sqlalchemy import String, Integer



# Diretório dos arquivos CSV
dir = 'D:\\Projetos\\Projeto\\'
list_files = os.listdir(dir)
print(list_files)

# Mapeamento dos nomes das colunas
colunas = {
    'coluna1': 'munic_id',
    'coluna2': 'ano',
    'coluna3': 'sexo_id',
    'coluna4': 'situacao_id',
    'coluna5': 'fxetaria_id',
    'coluna6': 'populacao'
}

# Dicionário para armazenar os DataFrames
dict_df = {}

# Ler arquivos CSV e renomear colunas
for file in list_files:
    if '.csv' in file:
        nome_tabela = file.split(".")[0]
        nome_tabela_min = nome_tabela.lower()
        tabela = pd.read_csv(file, delimiter=",", header=None, skiprows=1, names=colunas.values(), dtype={'munic_id': str, 'ano': int, 'sexo_id': int, 'situacao_id': str, 'fxetaria_id':int, 'populacao': int})
        dict_df[nome_tabela_min] = tabela

# Conexão com o banco de dados MySQL
db_connection_str = f"mysql+mysqlconnector://root:112233@localhost/projeto1"
db_connection = create_engine(db_connection_str)

# Importar DataFrames nas tabelas MySQL
for table_name, table_df in dict_df.items():
    table_df.to_sql(table_name, con=db_connection, if_exists='replace', index=False)



# import libs
import wget
import os
import zipfile
from ftplib import FTP




ftp = FTP("ftp.datasus.gov.br")
ftp.login() # É necessário usar o .login para conseguir acessar o FTP. O padrão é vazio, assim entrará como anônimo.

ftp.cwd("/dissemin/publicos/IBGE/POP/")  # Navega até o diretório desejado

file_list = ftp.nlst()  # Obtém a lista de arquivos no diretório



### Variables ####

dir = 'D:\\Projetos\\Projetos\\Brazilian_Census\\'
files_dir = os.listdir(dir)

# file_to_download = 'ftp://ftp.datasus.gov.br/dissemin/publicos/IBGE/POP/'





try: 
    for filename in file_list:
        if filename in files_dir:
            print(f'{filename} - Already Downloaded')
        else:
            file_to_download = f'ftp://ftp.datasus.gov.br/dissemin/publicos/IBGE/POP/{filename}'
            wget.download(file_to_download, out=dir)
        with zipfile.ZipFile(f'{dir}{filename}', 'r') as zip_ref:
            csv_filename = filename.replace('.zip','.csv')
            if csv_filename in zip_ref.namelist():
                zip_ref.extract(csv_filename)

except EOFError as e:
    print(e)





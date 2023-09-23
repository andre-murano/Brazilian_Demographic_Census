from ftplib import FTP




ftp = FTP("ftp.datasus.gov.br")
ftp.login() # É necessário usar o .login para conseguir acessar o FTP. O padrão é vazio, assim entrará como anônimo.

ftp.cwd("/dissemin/publicos/IBGE/POP/")  # Navega até o diretório desejado

file_list = ftp.nlst()  # Obtém a lista de arquivos no diretório

for filename in file_list:
    print(filename)



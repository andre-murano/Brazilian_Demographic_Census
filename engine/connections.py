# import libs
import wget

# get file from FTP
try:
    wget.download('ftp://ftp.datasus.gov.br/cnes/BASE_DE_DADOS_CNES_201805.ZIP')
except:
    print('aoba')



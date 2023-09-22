# import libs
import wget
import io
import os
import sys
import datetime
import zipfile
import stat

# variables

pattern_file = 'POPBR12.zip'
file_to_download = f'ftp://ftp.datasus.gov.br/dissemin/publicos/IBGE/POP/{pattern_file}'
dir = f'C:\\Users\\andre\PycharmProjects\Projeto\\'
list_files = os.listdir(dir)
# os.chmod(dir, stat.S_IRWXU)

print(list_files)

# get file from FTP
try:
    if pattern_file in list_files:
        print('Already Downloaded')
    else:
        wget.download(file_to_download, out=dir)
    with zipfile.ZipFile(f'{dir}{pattern_file}', 'r') as zip_ref:
        zip_ref.extractall(f'{dir}')
    # for file_name in os.listdir(dir):
    #     if pattern_file != file_name and file_name != '.idea':
    #          os.remove(f'{dir}{file_name}')

except EOFError as e:
    print(e)
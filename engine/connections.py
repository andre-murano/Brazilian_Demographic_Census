# import libs
import wget
import io
import os
import sys
import datetime
import zipfile

# variables
year = datetime.date.today() - datetime.timedelta(days=30)
year = year.strftime("%Y%m")

pattern_file = f"FORNEC_{year}.ZIP"
file_to_download = f'ftp://ftp.datasus.gov.br/cnes/{pattern_file}'
dir = f"D:\Projetos\public-health\incoming_files\\"
list_files = os.listdir(dir)

print(list_files) 

# get file from FTP
try:
    if pattern_file in list_files:
        print('Already Downloaded')
    else:
        wget.download(file_to_download, out=dir)
        with zipfile.ZipFile(f'{dir}{pattern_file}', 'r') as zip_ref:
            zip_ref.extractall(f'{dir}')
except EOFError as e:
    print(e) 
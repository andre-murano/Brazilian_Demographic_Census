
#Download the file with guidance on fact table columns

import wget
import os
import zipfile
from ftplib import FTP




ftp = FTP("ftp.datasus.gov.br")
ftp.login() 

ftp.cwd("/dissemin/publicos/IBGE/doc/")  

guidance_table = 'populacao.pdf'


with open(guidance_table, 'wb') as arquivo:
    ftp.retrbinary('RETR ' + guidance_table, arquivo.write)




#Building the dim_tables







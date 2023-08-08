import pandas as pd

df1 = pd.read_csv(filepath_or_buffer='D:\Projetos\public-health\incoming_files\Fornec.txt',header=1,delimiter='\\t')
print(df1.head(10))
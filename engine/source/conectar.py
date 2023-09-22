import mysql.connector

def criar_conexao(host, user, password, database):
    return mysql.connector.connect(
    host='localhost',
    user='root',
    password='112233',
    database='projeto'
    )

def fechar_conexao(con):
    return con.close()

def cursor():
    return criar_conexao('host', 'user', 'password', 'database').cursor()

cursor().execute('CREATE TABLE')

# bd = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='112233',
#     database='projeto'
#     )
#
# cursor = bd.cursor()
#
# cursor.execute("USE carros;"
#     "CREATE TABLE marcas("
# 	"marcas_id INT NOT NULL AUTO_INCREMENT,"
#     "PRIMARY KEY(marcas_id)"
# ");"
# )
#


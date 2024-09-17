import mysql.connector

def Conexao():
    conexao = mysql.connector.connect(host='localhost',
                                        database='DbSistemaBancario',
                                        user='root',
                                        password='12345678')
    return conexao
    

conexao = Conexao()
def Cursor():
    cursor = conexao.cursor()
cursor = Cursor()

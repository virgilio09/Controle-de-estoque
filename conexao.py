import mysql.connector as mysql

def conexao(conectar):

   
    if(conectar):
        conexao = mysql.connect(host = 'localhost', db = 'poo2', user='root', passwd = '')
        cursor = conexao.cursor()

        return conexao 
    
    else: 
        conexao.commit()
        conexao.close()
        return False
    


print(conexao(True))


print(conexao(False))



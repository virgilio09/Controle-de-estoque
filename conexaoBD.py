import mysql.connector as mysql


class Conexao():

    def __init__(self, host = 'localhost',  db = 'estoque', user = 'root', passwd = ''):
        self.host = host
        self.db = db
        self.user = user
        self.passwd = passwd
    
    def conecta(self):
       
        self.con = mysql.connect(host = self.host,  db = self.db, user = self.user, passwd = self.passwd)
        self.cursor = self.con.cursor()
                  
    #  comandos que interação
    def executaDML(self, sql):
        self.conecta()
        self.cursor.execute(sql)
        self.con.commit()
        self.con.close()

    # comandos de consulta
    def executaDQL(self, sql):
        self.conecta()
        self.cursor.execute(sql)
        resp = self.cursor.fetchall()
        self.con.close()

        return resp

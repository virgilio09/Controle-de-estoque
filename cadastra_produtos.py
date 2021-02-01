from conexaoBD import Conexao

class Cadastra_prond:

	def __init__(self):
		self.con = Conexao()

	def insere(self, nome, valor, qtd):

		sql = 'INSERT INTO produto(nome, valor, quantidade) VALUES("%s", %.2f, %d)'%(nome, valor, qtd)
		self.con.executaDML(sql)
		

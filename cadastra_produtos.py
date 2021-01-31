from conexaoBD import Conexao

class Cadastra_func:
	'''
	class Cadastra_func()
	Realiza o cadastro dos funcionários em lista diferente das dos clientes.
	'''
	def __init__(self):
		self.con = Conexao()

	def insere(self, nome, cpf, salario, senha):

		resp = self.busca_cpf(cpf)
		
		if(resp == None):
			sql = 'INSERT INTO funcionario(nome, cpf, salario, senha) VALUES("%s", "%s", %.2f, MD5("%s"))'%(nome, cpf, salario, senha)
			print(sql)
			self.con.executaDML(sql)
		
		else:
			return False

	def busca_cpf(self, cpf):
		
		self.con.conecta
	
		resp = self.con.executaDQL('SELECT nome, cpf, salario FROM funcionario WHERE cpf = "%s"' %cpf)

		if(resp != []):
			return resp
		else:
			return None
	

class Cadastra_cli:
	
	def __init__(self):
		self.con = Conexao()

	def insere(self, nome, cpf):

		resp = self.busca_cpf(cpf)
		
		if(resp == None):
			sql = 'INSERT INTO cliente(nome, cpf) VALUES("%s", "%s")'%(nome, cpf)
			self.con.executaDML(sql)
		
		else:
			return False

	def busca_cpf(self, cpf):
		
		self.con.conecta
	
		resp = self.con.executaDQL('SELECT nome, cpf FROM cliente WHERE cpf = "%s"' %cpf)

		if(resp != []):
			return resp
		else:
			return None

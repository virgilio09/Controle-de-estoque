from estoque import Estoque
from funcionario import Funcionario
from cliente import Cliente

class Loja():
	
	def __init__(self):
		self._nome = None
		self._list_funcionarios = []
		self._list_clietes = []
		self.estoque = Estoque()

	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, nome):
		self._nome = nome


	def cadastra_func(self):
		func = Funcionario()
		func.nome = input("Nome: ")
		func.cpf = input("CPF: ")
		func.salario = float(input("Salario: "))

	def cadastra_cliente(self):
		cliente = Cliente()
		cliente.nome = input("Nome: ")
		cliente.cpf = input("CPF: ")


	def comprar_produtos():
		pass		
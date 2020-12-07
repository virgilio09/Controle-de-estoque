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
		self._list_funcionarios.append(func)

	def cadastra_cliente(self):
		cliente = Cliente()
		cliente.nome = input("Nome: ")
		cliente.cpf = input("CPF: ")
		self._list_clietes.append(cliente)

	def buscar_funcionario(self):
		cpf = input("Digite seu cpf: ")
		resultado = [func for func in self._list_funcionarios if func.cpf == cpf]
		return resultado
	
	def analise_compras(self, Cliente):
		if(Cliente.carrinho != []):
			self.cupom_fiscal(Cliente)
			op = input("\nDeseja aprovar esta compra?(S/N)").lower()
			if(op == 's'):
				func = self.buscar_funcionario()
				if(func != []):
					print("Compra aprovada com sucesso!\n")
				else:
					print("\nCpf incorreto!\n")
			else:
				print("Compra cancelada!")

	def cupom_fiscal(self, Cliente):
	
		if(Cliente.carrinho != []):
			print("---- Cupom fiscal ----")
			for produto in Cliente.carrinho:
				print("Código	Produto		Valor unit.\n")
				print("{}	{}		{}".format(produto.codigo, produto.nome, produto.valor))

			Cliente.total_carrinho()



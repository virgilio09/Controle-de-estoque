from estoque import Estoque
from funcionario import Funcionario
from cliente import Cliente

class Loja():
	
	def __init__(self):
		self._nome = None
		self._list_funcionarios = []
		self._list_clientes = []
		self._estoque = Estoque()

	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, nome):
		self.nome = nome

	@property
	def estoque(self):
		return self._estoque

	@estoque.setter
	def estoque(self, estoque):
		self._estoque = estoque
	
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
		self._list_clientes.append(cliente)

	def buscar_funcionario(self):
		cpf = input("Digite seu cpf: ")
		resultado = [func for func in self._list_funcionarios if func.cpf == cpf]
		return resultado
	
	def buscar_cliente(self):
		cpf = input("\nDigite cpf do Cliente: ")
		resultado = [cliente for cliente in self._list_clientes if cliente.cpf == cpf]
		return resultado
	
	def remove_cliente(self):
		
		result = self.buscar_cliente()

		if(result != []):
			self._list_clientes.remove(result[0])
			print("Cliente removido com sucesso!\n")
		else:
			print("Cliente não cadastrado!\n")
			

	def remove_func(self):
		result = self.buscar_funcionario()

		if(result != []):
			self._list_funcionarios.remove(result[0])
			print("Funcionario removido com sucesso!\n")
		else:
			print("Funcionario não cadastrado!\n")

	def mostrar_clientes(self):
		if(self._list_clientes != []):
			print("---- Lista de Clientes ----")
			for cliente in self._list_clientes:
				print("Nome: {}".format(cliente.nome))
				print("Cpf: {}".format(cliente.cpf))
				print("-"*20)
		else:
			print("Cadastro vazio!")

	def mostrar_func(self):
		if(self._list_funcionarios != []):
			print("---- Lista de Funcionarios ----")
			for func in self._list_funcionarios:
				print("\nNome: {}".format(func.nome))
				print("Cpf: {}".format(func.cpf))
				print("Salario: {}".format(func.salario))
				print("-"*20)
		else:
			print("Cadastro vazio!")


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
from pessoa import Pessoa
from estoque import Estoque

class Cliente(Pessoa): 
	
	_qtd_clientes = 0

	def __init__(self):
		super().__init__()
		self._carrinho = []
		Cliente._qtd_clientes += 1

	@staticmethod
	def get_qtd_clientes():
		return Cliente._qtd_clientes


	@property
	def carrinho(self):
		return self._carrinho

	# adicionar ao carrinho
	def add_produto(self,Estoque):
		
		produto = Estoque.buscar_produto()
		adicionou = False  
		
		if(produto != []):
			self._carrinho.append(produto[0])
			print("Produto adicionado com sucesso!")
			adicionou = True
		else:
			print("Produto não encontrado no estoque!")

		return adicionou

	# remover do carrinho
	def rm_produto(self):
		
		codigo = input("Codigo do produto: ")

		if(self._carrinho != []):

			for produto in self._carrinho:
				if(produto.codigo == codigo):
					self._carrinho.remove(produto)
					print("Produto removido com sucesso!")
					return True

			print("Produto não encontrado no carrinho!")
			return False
		else:
			print("O carrinho está vaziu")

	# valor total dos produtos no carrinho
	def total_carrinho(self):

		if(self._carrinho != []):

			total = 0;

			for produto in self_carrinho:
				total += produto.valor

			print("Total = {0:4.2f}".format(total))

		else:
			print("O carrinho está vaziu")
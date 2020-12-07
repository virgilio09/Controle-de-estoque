from pessoa import Pessoa
from estoque import Estoque

class Cliente(Pessoa): 
	
	_total_compras = 0

	def __init__(self):
		super().__init__()
		self._carrinho = []


	@property
	def carrinho(self):
		return self._carrinho


	# adicionar ao carrinho
	def add_produto(self,Estoque):
		produto = Estoque.buscar_produto()
		if(produto != []):
			self._carrinho.append(produto[0])
			print("Produto adicionado com sucesso!")
			return 1
		else:
			print("Produto não encontrado no estoque!")
			return 0

	# remover do carrinho
	def rm_produto(self):
		pass


	def total_carrinho(self):
		pass
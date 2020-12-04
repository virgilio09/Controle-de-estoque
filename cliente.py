from pessoa import Pessoa

class Cliente(Pessoa): 
	
	def __init__(self):
		super().__init__()
		self._carrinho = [] 

	@property
	def carrinho(self):
		return self._carrinho


	# adicionar ao carrinho
	def add_produto(self):
		pass

	# remover do carrinho
	def rm_produto(self):
		pass


	def total_carrinho(self)
		pass
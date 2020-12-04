from pessoa import Pessoa

class Cliente(Pessoa): 
	
	def __init__(self):
		super().__init__()
		self._carrinho = [] 


	@property
	def carrinho(self):
		return self._carrinho

from pessoa import Pessoa
from estoque import Estoque
from carrinho import Carrinho

class Cliente(Pessoa): 
	
	_qtd_clientes = 0

	def __init__(self):
		super().__init__()
		self._carrinho = Carrinho()
		Cliente._qtd_clientes += 1

	@staticmethod
	def get_qtd_clientes():
		return Cliente._qtd_clientes


	@property
	def carrinho(self):
		return self._carrinho

	@carrinho.setter
	def carrinho(self, carrinho):
		self._carrinho = carrinho


	# adicionar ao carrinho
	def add_produto(self,Estoque):
		
		produto = Estoque.buscar_produto()
		adicionou = False  
		
		if(produto != []):
			qtd = input("Quantidade do produto que deseja adiconar: ")
			quant = int(qtd)
			produto[0].quantidade -= quant
			self._carrinho._lista_produtos.append(produto[0])
			self._carrinho.quantidade.append(quant)
			print("Produto adicionado com sucesso!")
			adicionou = True
		else:
			print("Produto não encontrado no estoque!")

		return adicionou

	# remover do carrinho
	def rm_produto(self):
		
		codigo = input("Codigo do produto: ")

		if(self._carrinho.lista_produtos != []):

			for produto in self._carrinho.lista_produtos:
				if(produto.codigo == codigo):
					indice = self._carrinho.lista_produtos.index(produto)
					self._carrinho.lista_produtos.remove(produto)
					del(self._carrinho.quantidade[indice])
					
					print("Produto removido com sucesso!")
					return True

			print("Produto não encontrado no carrinho!")
			return False
		else:
			print("O carrinho está vaziu")

	# valor total dos produtos no carrinho
	def total_carrinho(self):

		if(self._carrinho != []):

			total = 0

			for produto in self._carrinho.lista_produtos:
				total += produto.valor

			print("Total = {0:4.2f}".format(total))

		else:
			print("O carrinho está vazio")
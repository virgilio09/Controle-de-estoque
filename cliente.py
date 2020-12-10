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
			print("\nAguarde a aprovação do vendedor!")
			adicionou = True
		else:
			print("Produto não encontrado no estoque!")

		return adicionou

	# remover do carrinho
	def rm_produto(self, Estoque):
		decisao = input("Deseja retirar todos os produtos(S/N)? ").lower()
		if(decisao == 's'):
			self.rm_carrinho_loja(Estoque)
			print("Todos os seus produtos foram removidos!\n")
		else:
			if(self._carrinho.lista_produtos != []):
				codigo = input("Codigo do produto: ")

				for produto in self._carrinho.lista_produtos:
					if(produto.codigo == codigo):
						indice_car = self._carrinho.lista_produtos.index(produto)
						indice_est = Estoque.lista_produtos.index(produto)
						if(self.carrinho.quantidade[indice_car] > 1):
							quant = int(input("Digite a quantidade a ser removida: "))
							self.carrinho.quantidade[indice_car] -= quant
							Estoque.lista_produtos[indice_est].quantidade += quant
							return True
						else:
							for prod in Estoque.lista_produtos:
								if(prod.codigo == codigo):
									prod.quantidade += 1
									return True

						print("Produto removido com sucesso!")
						return True

				print("Produto não encontrado no carrinho!")
				return False
			else:
				print("O carrinho está vazio")

	#remove produto do carrinho para o estoque da loja.
	def rm_carrinho_loja(self, Estoque):
		for produto in self.carrinho.lista_produtos:
			indice = self.carrinho.lista_produtos.index(produto)
			
			for prod in Estoque.lista_produtos:
				prod.quantidade += self.carrinho.quantidade[indice]
				del(self.carrinho.quantidade[indice])
				del(self.carrinho.lista_produtos[indice])


	# valor total dos produtos no carrinho
	def total_carrinho(self):

		if(self._carrinho != []):

			total = 0

			for produto in self._carrinho.lista_produtos:
				indice = self._carrinho.lista_produtos.index(produto)
				total += produto.valor * self.carrinho.quantidade[indice]

			print("\nTotal = {0:4.2f}".format(total))

		else:
			print("O carrinho está vazio")
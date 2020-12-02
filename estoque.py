from produto import Produto

class Estoque:

	def __init__(self):
		self._lista_produtos = []


	@property
	def lista_produtos(self):
		return self._lista_produtos
	


	def cadastrar_produto(self):
		
		produto = Produto() # cria objeto da classe produto

		produto.codigo = input("Codigo: ")
		produto.nome = input("Nome: ")
		produto.valor = float(input("valor: "))
		Produto.data_validade = input("Data de validade: ")
	
		self._lista_produtos.append (produto)


	def mostrar_produtos(self, lista_produtos):

		if(lista_produtos != []):
			print("--- Lista de Produtos ----\n")
			for produto in lista_produtos:
				print("Código: {}".format(produto.codigo))
				print("Nome: {}".format(produto.nome))
				print("Valor: {0:4.2f}".format(produto.valor))
				print("Data de validade: {}\n".format(produto.data_validade))
		else:
			print("O Estoque está vaziu\n")


	
	def buscar_produto(self):

		codigo = input("Código do produto: ")

		result = [produto for produto in self._lista_produtos if produto.codigo == codigo]
		
		return result

	def remover_produto(self):
		
		result = self.buscar_produto()

		if(result != []):
			self._lista_produtos.remove(result[0])
			print("Produto removido com sucesso")

		else:
			print("Produto não exite no estoque")
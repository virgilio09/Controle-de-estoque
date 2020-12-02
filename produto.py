class Produto:
	
	def __init__(self):
		self._codigo = 0
		self._nome = None
		self._valor = 0
		self._data_validade = None


	@property
	def codigo(self):
		return self._codigo

	@codigo.setter
	def codigo(self, codigo):
		self._codigo = codigo


	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, nome):
		self._nome = nome

	@property
	def valor(self):
		return self._valor

	@valor.setter
	def valor(self):
		if(valor >= 0):
			self._valor = valor
		
		else:
			print("Valor invalido\n")


	@property
	def data_validade(self):
		return self._data_validade

	
	@data_validade.setter
	def data_validade(self, data_validade):
		self._data_validade = data_validade
class Pessoa:
	
	def __init__(self):
		self._nome = None
		self._cpf = None
		self._endereco = None

	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, nome):
		self._nome = nome

	@property
	def cpf(self):
		return self._cpf

	@cpf.setter
	def cpf(self, cpf):
		self._cpf = cpf

	@property
	def endereco(self):
		return self._endereco


	@endereco.setter
	def endereco(self, endereco):
		self._endereco = endereco
	
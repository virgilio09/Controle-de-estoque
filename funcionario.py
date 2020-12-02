class Funcionario(object):
	
	def __init__(self, pessoa):
		self._info = pessoa
		self._setor = None

	@property
	def setor(self):
		return self._setor

	@setor.setter
	def setor(self, setor):
		self._setor = setor
	

		
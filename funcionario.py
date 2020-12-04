
from pessoa import Pessoa

class Funcionario(Pessoa):
	
	def __init__(self, pessoa):
		super().__init__()
		self._setor = None

	@property
	def setor(self):
		return self._setor

	@setor.setter
	def setor(self, setor):
		self._setor = setor
	

		
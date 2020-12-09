from estoque import Estoque
from produto import Produto


class Carrinho(Estoque):
    def __init__(self):
        self._lista_produtos = []
        self._quantidade = []

    @property
    def lista_produtos(self):
        return self._lista_produtos

    @property
    def quantidade(self):
        return self._quantidade

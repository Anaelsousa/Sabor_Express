from Modelos.Avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    @property
    def ativo(self):
        return "ativado" if self._ativo else "desativado"

    def __str__(self):
        return f"{self._nome}, {self._categoria}, {self.ativo}"

    @classmethod
    def listar_restaurantes(cls):
        print(f"{"Nome".ljust(25)} - {"Categoria".ljust(25)} - {"Avaliação".ljust(25)} - Estatos")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} - {restaurante._categoria.ljust(25)} - {restaurante.media_avaliacoes} - {restaurante.ativo}")

    def ativar_desativar_restaurante(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "Ainda não áh avaliações"
        else:
            soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
            return round(soma_das_notas / len(self._avaliacao), 1)

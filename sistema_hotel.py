class Hotel:
    def __init__(self, nome, endereco, quartos):
        self.nome = nome
        self.endereco = endereco
        self.quartos = []

    def get_quartos_disponiveis(self, data_entrada, data_saida):
        return
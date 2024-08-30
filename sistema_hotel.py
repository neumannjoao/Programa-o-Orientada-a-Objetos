class Hotel:
    def __init__(self, nome, reservas, quartos):
        self.nome = nome
        self.reservas = []
        self.quartos = []

    def adicionar_quarto (self,quartos):
        self.quartos.append(quarto)

    #Fazer uma Reserva
    def fazer_reserva(self, cliente, numQuarto, data_entrada, data_saida):
        for quarto in self.quartos:
            if numQuarto

    #Fazer Checkout

class Quarto:
    def __init__(self, numQuarto, tipo):
        self.numQuarto: numQuarto
        self.tipo = tipo
        self.ocupado = False

    def marcar_disponível (self, ocupado):
        self.ocupado = False

    def marcar_ocupado (self, ocupado):
        self.ocupado = True

class Cliente:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento

class Reserva:
    def __init__(self, cliente, quarto, data_entrada, data_saida):
        self.cliente = cliente
        self.quarto = quarto
        self.data_entrada = data_entrada
        self.data_saida = data_saida

    def confirmar(self):
        self.quarto.marcar_ocupado()


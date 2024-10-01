class Carro:
    def __init__(self,marca, ano):
        self.marca = marca
        self.__ano = ano

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):   
        if ano< 1885:
            print("Ano inválido, insira outro ano")
        else:
            self.__ano = ano 

    def exibir(self):
        print(f"A marca do carro é {self.marca}.")
        print(f"O ano do carro é {self.ano}.")

class carroEletrico (Carro):
    def __init__ (self, marca, ano )

carro1 = Carro ("Volks", 2020)

carro1.exibir()
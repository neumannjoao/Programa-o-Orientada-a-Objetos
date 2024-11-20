class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"O valor do ingresso é: R${self.valor:.2f}")

class VIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional
    
    def valorVIP(self):
        return self.valor + self.adicional
    
class Normal(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def imprimeValor(self):
        print("Ingresso Normal")
        super().imprimeValor()

class CamaroteInferior(VIP):
    def __init__(self, valor, adicional, localizacao):
        super().__init__(valor, adicional)
        self.localizacao = localizacao

    def imprimeLocalizacao(self):
        print(f"A localização do Camarote Inferior é: {self.localizacao}")

    def imprimeValor(self):
        super().imprimeValor()
        print(f"Valor do ingresso Camarote Inferior: R${self.valorVIP():.2f}")

class CamaroteSuperior(VIP):
    def __init__(self, valor, adicional, adicional_superior):
        super().__init__(valor, adicional)
        self.adicional_superior = adicional_superior

    def valorCamaroteSuperior(self):
        return self.valorVIP() + self.adicional_superior

    def imprimeValor(self):
        super().imprimeValor()
        print(f"Valor do ingresso no Camarote Superior: R${self.valorCamaroteSuperior():.2f}")

def main():
    tipo_ingresso = int(input("1 - Ingresso Normal \n 2 - Ingresso VIP \n Escolha o tipo do seu ingresso: "))

    if tipo_ingresso == 1:
        valor_normal = float(input("Digite o valor do ingresso normal: R$"))
        ingresso_normal = Normal(valor_normal)
        ingresso_normal.imprimeValor()

    elif tipo_ingresso == 2:
        valor_vip = float(input("Digite o valor do ingresso VIP: R$"))
        adicional_vip = float(input("Digite o valor adicional do ingresso VIP: R$"))
        ingresso_vip = VIP(valor_vip, adicional_vip)

        tipo_camarote = int(input("Digite 1 para Camarote Superior ou 2 para Camarote Inferior: "))

        if tipo_camarote == 1:
            adicional_superior = float(input("Digite o valor adicional para o Camarote Superior: R$"))
            camarote_superior = CamaroteSuperior(valor_vip, adicional_vip, adicional_superior)
            camarote_superior.imprimeValor()

        elif tipo_camarote == 2:
            localizacao_inferior = input("Digite a localização do Camarote Inferior: ")
            camarote_inferior = CamaroteInferior(valor_vip, adicional_vip, localizacao_inferior)
            camarote_inferior.imprimeLocalizacao()
            camarote_inferior.imprimeValor()

if __name__ == "__main__":
    main()

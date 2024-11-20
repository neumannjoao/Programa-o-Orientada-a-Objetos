class Forma:
    def desenhar(self):
        pass

class FormaBidimensional(Forma):
    def getArea(self):
        pass

class FormaTridimensional(Forma):
    def getArea(self):
        pass

    def getVolume(self):
        pass

class Quadrado(FormaBidimensional):
    def __init__(self, lado, caractere):
        self.lado = lado
        self.caractere = caractere

    def getArea(self):
        return self.lado * self.lado  # Área = lado x lado

    def desenhar(self):
        for i in range(self.lado):
            print(self.caractere * self.lado)

class Circulo(FormaBidimensional):
    def __init__(self, raio, caractere):
        self.raio = raio
        self.caractere = caractere

    def getArea(self):
        return 3.1416 * self.raio * self.raio  # Área = pi * raio²

    def desenhar(self):
        for i in range(-self.raio, self.raio + 1):
            for j in range(-self.raio, self.raio + 1):
                if i * i + j * j <= self.raio * self.raio:
                    print(self.caractere, end="")
                else:
                    print(" ", end="")
            print()

class Cubo(FormaTridimensional):
    def __init__(self, lado, caractere):
        self.lado = lado
        self.caractere = caractere

    def getArea(self):
        return 6 * (self.lado ** 2)  # Área = 6 * lado² (6 faces)

    def getVolume(self):
        return self.lado ** 3  

    def desenhar(self):
        for i in range(self.lado):
            print(self.caractere * self.lado)

class Esfera(FormaTridimensional):
    def __init__(self, raio, caractere):
        self.raio = raio
        self.caractere = caractere

    def getArea(self):
        return 4 * 3.1416 * (self.raio ** 2)  # area = 4 * pi * raio²

    def getVolume(self):
        return (4 / 3) * 3.1416 * (self.raio ** 3)  

    def desenhar(self):
        for i in range(-self.raio, self.raio + 1):
            for j in range(-self.raio, self.raio + 1):
                if i * i + j * j <= self.raio * self.raio:
                    print(self.caractere, end="")
                else:
                    print(" ", end="")
            print()

def main():
    formas = [
        Quadrado(3, 'X'),
        Circulo(4, 'A'),
        Cubo(3, 'O'),
        Esfera(2, 'O')
    ]
    
    for forma in formas:
        print(f"Classe: {forma.__class__.__name__}")
        
        if isinstance(forma, FormaBidimensional):
            print("Tipo: Forma Bidimensional")
            print(f"Área: {forma.getArea()}")
            forma.desenhar()
        elif isinstance(forma, FormaTridimensional):
            print("Tipo: Forma Tridimensional")
            print(f"Área: {forma.getArea()}")
            print(f"Volume: {forma.getVolume()}")
            forma.desenhar()
        print()

if __name__ == "__main__":
    main()

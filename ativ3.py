class Pessoa:
    def __init__(self, nome, sexo, idade, altura, peso):
        if sexo not in {'M', 'F'}:
            raise ValueError("Sexo inválido. Use 'M' ou 'F'.")
        
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.altura = altura
        self.peso = peso
        
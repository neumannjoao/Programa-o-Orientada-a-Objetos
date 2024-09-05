<<<<<<< HEAD
class Pessoa:
    def __init__(self, nome, sexo, corOlhos, pai=None, mae=None):
        self.nome=nome
        self.sexo=sexo
        self.corOlhos=corOlhos
        self.pai=pai
        self.mae=mae

    #verificar sxo e a cor dos olhos

    def verificar(sexo, corOlhos):
        if sexo not in ['M', 'F']:
            return("Sexo inválido. Use 'M' para masculino ou 'F' para feminino.")

        if corOlhos not in ['C', 'V', 'A']:
            return("Cor dos Olhos inválida. Use 'C' para castanho, 'V' para verde e 'A' para azul")
    
    def gera_pessoa(self, nome, sexo, pai):
        if self.sexo != 'F' or pai.sexo != 'M':
            print('Não é possível criar uma nova pessoa com esses parâmetros.')
            return None

        cor_olhos_mae = self.corOlhos if self.mae else 'A'
        cor_olhos_pai = pai.corOlhos
        cor_olhos_filho = self.determinar_cor_olhos(cor_olhos_mae, cor_olhos_pai)

        return Pessoa(nome, sexo)

    def determinar_cor_olhos(self, cor_pai, cor_mae):
        if cor_pai == 'C' or cor_mae == 'C':
            return 'C'
        if cor_pai == 'V' or cor_mae == '':
            return 'V'
        return 'A'

    def get_sexo_str(self):
        return 'Masculino' if self.sexo == 'M' else 'Feminino'

    def get_cor_olhos_str(self):
        if self.corOlhos == 'C':
            return 'Castanho'
        if self.corOlhos == 'V':
            return 'Verde'
        if self.corOlhos == 'A':
            return 'Azul'

    def imprime_dados(self):
        print('imprimindo dados...')
    

    imprime_dados()
    
=======
class Pessoa:
    def __init__(self, nome, sexo, corOlhos, pai=None, mae=None):
        self.nome=nome
        self.sexo=sexo
        self.corOlhos=corOlhos
        self.pai=pai
        self.mae=mae

    #verificar sxo e a cor dos olhos
    if sexo not in ['M', 'F']:
        raise ValueError("Sexo inválido. Use 'M' para masculino ou 'F' para feminino.")

    if corOlhos not in ['C', 'V', 'A']:
        raise ValueError("Cor dos Olhos inválida. Use 'C' para castanho, 'V' para verde e 'A' para azul")
    
    def gera_pessoa(self, nome, sexo, pai):
        if self.sexo != 'F' or pai.sexo != 'M':
            print('Não é possível criar uma nova pessoa com esses parâmetros.')
            return None

        cor_olhos_mae = self.corOlhos if self.mae else 'A'
        cor_olhos_pai = pai.corOlhos
        cor_olhos_filho = self.determinar_cor_olhos(cor_olhos_mae, cor_olhos_pai)

        return Pessoa(nome, sexo)

    def determinar_cor_olhos(self, cor_pai, cor_mae):
        if cor_pai == 'C' or cor_mae == 'C'
        return 'C'
        if cor_pai == 'V' or cor_mae == ''
        return 'V'
    return 'A'

    def get_sexo_str(self):
        return 'Masculino' if self.sexo == 'M' else 'Feminino'

    def get_cor_olhos_str(self):
        if self.corOlhos == 'C':
            return 'Castanho'
        if self.corOlhos == 'V':
            return 'Verde'
        if self.corOlhos == 'A':
            return 'Azul'

    def imprime
>>>>>>> e008edda7ad9af2d21526b34244363fbab499358

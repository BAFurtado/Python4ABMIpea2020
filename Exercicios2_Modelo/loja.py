from Exercicios2_Modelo.conta import Conta


class Loja:
    def __init__(self, id):
        self.id = id
        self.conta = Conta(0)
        self.custo_produto = 10


if __name__ == '__main__':
    arezzo = Loja('shopping_conjunto')
    big_box = Loja('big_box')

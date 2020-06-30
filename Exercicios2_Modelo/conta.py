

class Conta:

    def __init__(self, id):
        self.id = id
        self.saldo = 0

    def deposito(self, quantia):
        self.saldo += quantia

    def retirada(self, quantia):
        self.saldo -= quantia
        return quantia


if __name__ == '__main__':
    bb = Conta(51980011100)
    bb.deposito(100)
    bb.deposito(100)
    # Pergunta: eu quero aceitar negativo?
    bb.deposito(-58)



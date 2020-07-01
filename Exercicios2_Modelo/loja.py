# Sugiro que depois o random seja colocado lá na simulation.py e você já traga o número de cada loja
import random
from Exercicios2_Modelo.conta import Conta


class Loja:
    def __init__(self, id):
        self.id = id
        self.conta = Conta(0)
        # Exemplo do uso da função round, 2 é a precisão do decimal.
        self.custo_produto = round(random.random() * 10, 2)
        self.experiencia = random.randint(0, 10)
        self.capacidade = random.randint(5, 200)

    def visita_cliente(self):
        # TODO: será necessário verificar se a capacidade já chegou a zero!
        # if self.capacidade <= 0: alternativamente, while self.capacidade >= 0, aceite clientes novos
        # return False (se não aceita capacidade). O return, break saem da função/while
        # TODO: continuar
        self.capacidade -= 1
        return True

    def ganha_experiencia(self):
        # Experiencia, nesse caso, refere-se à experiência do cliente ao usufruir do produto.
        # TODO: alguma hora, o agente vai visitar e deve-lhe ser retornado self.experience
        # TODO: altera a experiencia de acordo com a capacidade
        pass


if __name__ == '__main__':
    fast_shop = Loja('shopping_conjunto')
    big_box = Loja('big_box')
    pizza_do_tom_ze = Loja('pizza1')
    pizza_do_tom_ze.conta.deposito(100000)

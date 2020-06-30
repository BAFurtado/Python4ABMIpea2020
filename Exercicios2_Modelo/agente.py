from Exercicios2_Modelo.conta import Conta
from Exercicios2_Modelo.loja import Loja


class Agent:
    def __init__(self):
        # nome, idade
        # TODO: criar de saída uma conta para esse agente
        self.conta = Conta(0)


if __name__ == '__main__':
    big_box = Loja('big_box')
    xisto = Agent()
    # Teste de agente que verifica a funcionalidade do deposito
    fredegonda = Agent()
    fredegonda.conta.deposito(1000)
    # Código passo-a-passo, seguido do código direto
    # bolso_da_loja = fredegonda.conta.retirada(1000)
    # big_box.conta.deposito(bolso_da_loja)

    # Comentário da linha abaixo
    # 1. A resolução é sempre de fora para dentro em relação aos parenteses.
    # 2. O primeiro parenteses a ser resolvido é big_box.custo_produto. Nesse caso big_box.custo_produto = 10
    # 3. Segundo parenteses fredegonda.conta.retirada(10). Diminui o saldo (que está guardado) e retorna 10.
    # 4. big_box.conta.deposito(10)
    big_box.conta.deposito(fredegonda.conta.retirada(big_box.custo_produto))


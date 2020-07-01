from Exercicios2_Modelo.loja import Loja


class Simulacao:
    def __init__(self):
        # Ao criar o objeto, rode os seguintes comandos
        # 1. Crie uma lista vazia chamada lojas e guarde junto com o objeto Simulacao
        self.lojas = list()
        self.clientes = list()
        # 2. Popule essa lista, chamando a função dessa própria classe chamada criar_lojas, utilizando self.função()
        self.criar_lojas()

    def ler_arquivo_dados(self):
        # TODO: por fazer
        # with open('arquivo1.csv', 'r') as handler...
        pass

    def criar_lojas(self):
        for id in range(10):
            self.lojas.append(Loja(id))

    def criar_agentes(self):
        # TODO: criar agentes de modo similar à criação de lojas...
        pass

    def run_model(self):
        # TODO: fazer um loop com os agentes e comprar nas lojas
        # 1. Vai ter que visitar a loja, faz retirada (esta no cliente) e ganha experiencia (loja)
        pass


if __name__ == '__main__':
    minha_sim = Simulacao()

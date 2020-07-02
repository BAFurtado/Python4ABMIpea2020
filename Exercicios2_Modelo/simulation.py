import random
from Exercicios2_Modelo.loja import Loja
from Exercicios2_Modelo.agente import Agent


class Simulacao:
    def __init__(self):
        # Ao criar o objeto, rode os seguintes comandos
        # 1. Crie uma lista vazia chamada lojas e guarde junto com o objeto Simulacao
        # **** self.lojas é a lista de lojas da simulação
        self.lojas = list()
        # **** self.clientes é a lista de clientes da simulação
        self.clientes = list()
        # 2. Popule essa lista, chamando a função dessa própria classe chamada criar_lojas, utilizando self.função()
        # **** Lembrando para chamar uma FUNÇÃO DE DENTRO DA PROPRIA CLASSE, USE self.funcao1()
        self.criar_lojas()
        self.criar_agentes()
        self.deposito_inicial()

    def salvar_arquivo_dados(self):
        # TODO: por fazer
        # with open('arquivo1.csv', 'w') as handler as f:
            pass

    def criar_lojas(self):
        for id in range(10):
            self.lojas.append(Loja(id))

    def criar_agentes(self):
        # TODO: criar agentes de modo similar à criação de lojas...
        pass

    def media_experiencia(self):
        experiencia_somada = 0
        for client in self.clientes:
            experiencia_somada += client.experiencia
        return experiencia_somada / len(self.clientes)

    def deposito_inicial(self):
        for client in self.clientes:
            client.conta.deposito(random.randint(10, 20))

    def run_model(self):
        # Decidir se a visita a loja ocorre três vezes.
        # TODO: fazer um loop com os agentes e comprar nas lojas
        # 1. Vai ter que visitar a loja, faz retirada (esta no cliente) e ganha experiencia (loja)
        # Vai ter um loop dos agentes para visitar as lojas. Primeiro ele testa a capacidade
        # Se a capacidade return
        for client in self.clientes:
            # Escolhe uma loja aleatoria
            loja_escolhida = random.choice(self.lojas)
            # Verificar a capacidade
            posso_ir = loja_escolhida.visita_cliente()
            if posso_ir:
                # cliente compra da loja
                # Algo similar a essa linha abaixo:
                # big_box.conta.deposito(fredegonda.conta.retirada(big_box.custo_produto))
                # o cliente tem que receber experiencia
                # client.experiencia += loja_escolhida.experiencia
                pass
        return self.media_experiencia()


if __name__ == '__main__':
    minha_sim = Simulacao()
    media = minha_sim.run_model()


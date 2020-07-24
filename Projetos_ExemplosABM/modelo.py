import numpy as np
import random

from Projetos_ExemplosABM.motoristas import Motorista
from Projetos_ExemplosABM.postos import Posto

num_motoristas = 100
num_postos = 8
custo_inicial = 4
rodadas = 2


class Simulacao:
    def __init__(self):
        self.motoristas = list()
        self.postos = list()
        self.criar_agentes()
        self.custo_combustivel = custo_inicial
        self.passos()

    def criar_agentes(self):
        num_localizacoes = 2 * (num_motoristas * 2 + num_postos)
        localizacoes = list(np.random.randint(0, 100, num_localizacoes))
        for i in range(num_motoristas):
            locs = localizacoes.pop(), localizacoes.pop(), localizacoes.pop(), localizacoes.pop()
            self.motoristas.append(Motorista(locs))
        for j in range(num_postos):
            self.postos.append(Posto(localizacoes.pop(), localizacoes.pop()))

    def distancia_casa_trabalho_media(self):
        # TODO: William Araujo vai realizar...
        pass

    def roda_modelo(self):
        # Comportamento da oferta -- decisão dos preços
        for p in self.postos:
            pass
        # Comportamento da demanda -- decisão de abastecer dos motoristas
        for m in self.motoristas:
            m.escolhe_posto(self.postos)
            print(m.meu_posto)
        self.custo_combustivel = self.custo_combustivel * \
                                 random.choices(np.linspace(.9, 1.1, 10),
                                                weights=[.01, .04, .1, .1, .25, .25, .1, .1, .04, .01], k=1)[0]
        # TODO: Recolher valores gerais

    def passos(self):
        for i in range(rodadas):
            self.roda_modelo()



if __name__ == '__main__':
    minha_sim = Simulacao()

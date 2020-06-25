""" Class template
    Ipea's Python for agent-based modeling course
    """

import random


# class name typically Capital letter
class Pessoa:
    # Usually has an __init__ method called at the moment of instance creation
    def __init__(self, name, distancia):
        # Armazena os parâmetros de início dentro daquela instância
        # É comum ter uma ID de identificação única, ou nome
        self.id = name
        self.distancia = distancia

        # Pode conter containers, data structures
        self.members = dict()
        self.ranking = list()

        # Ou ainda, um valor randômico
        self.luck = random.randrange(1, 60)
        self.partner = None

    def adiciona_distancia(self, quantia):
        # Modifica um valor armazenado
        self.distancia += quantia

    def compara(self, outro_agente):
        # Pode comparar-se com outro agente e acessar métodos do outro agente
        if self.distancia > outro_agente.distancia:
            return True
        else:
            return False

    def adiciona_sorte(self):
        # Um método pode acessar um outro método.
        # Nesse caso, adicionando um valor aleatório ao arg1!
        self.adiciona_distancia(self.luck)

    def match(self, outro_agente):
        # Esse método recebe outro agente (dessa mesma classe) e guarda/adiciona/salva o outro agente como uma variavel,
        # dentro deste próprio agente
        self.partner = outro_agente
        outro_agente.partner = self


if __name__ == '__main__':
    tita = Pessoa('Tita', 10)
    max = Pessoa('Max', 20)
    fred = Pessoa('Fred', 0)
    aveia = Pessoa('Aveia', 11)
    print(aveia.compara(tita))
    max.match(aveia)

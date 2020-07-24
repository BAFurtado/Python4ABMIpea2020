import random


class Posto:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.preco = random.uniform(3.9, 4.1)

    def definir_preco(self):
        # TODO: Alan Dill
        pass

    def __repr__(self):
        return f'Posto no Quadra {self.x}, {self.y}'

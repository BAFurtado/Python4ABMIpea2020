import uuid


class Motorista:
    def __init__(self, locs):
        self.id = str(uuid.uuid4())[:8]
        self.casa_x, self.casa_y, self.trabalho_x, self.trabalho_y = locs

    def escolhe_posto(self):
        pass

    def dirigir(self):
        pass

    def calcular_distancia(self):
        pass

    def __repr__(self):
        return f'Motorista {self.id}'

if __name__ == '__main__':
    Maria = Motorista()

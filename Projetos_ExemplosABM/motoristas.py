import uuid
import random


class Motorista:
    def __init__(self, locs):
        self.id = str(uuid.uuid4())[:8]
        self.casa_x, self.casa_y, self.trabalho_x, self.trabalho_y = locs
        self.distancia = random.randint(500, 1500)
        self.meu_posto = None
        self.gasto = None
        self.preferencia = random.choices(['preco', 'distancia'], weights=[.8, .2], k=1)[0]

    def escolhe_posto(self):
        # Se a preferencia for preço, não preciso nem escolher a distância
        pass

    def dirigir(self):
        print(self.meu_posto.preco * self.distancia)

    def calcular_distancia(self, postos):
        # Escolho casa ou trabalho
        escolha = random.choices(['casa', 'trabalho'])
        distancias = list()
        for posto in postos:
            if escolha == 'casa':
                distancias.append(((posto.x - self.casa_x) ** 2 + (posto.y - self.casa_y) ** 2) ** .5)
            else:
                distancias.append(((posto.x - self.trabalho_x) ** 2 + (posto.y - self.trabalho_y) ** 2) ** .5)
        # Calculo distancia minima
        # Preciso retornar/descobrir qual é o posto mais perto para o meu caso
        return postos[distancias.index(min(distancias))]

    def __repr__(self):
        return f'Motorista {self.id}'


if __name__ == '__main__':
    Maria = Motorista()

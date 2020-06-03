


""" Script que calcula a área do círculo
    Exemplo de função comentada
    Python for ABM - Ipea - Maio 2020, em meio à pandemia
    """

import math


def outro_exemplo_comentado():

    """ Isso é um comentário
        de várias linhas
        """
    print('outro exemplo rodado com sucesso!')


def area_circle(r):
    """ Função que calcula área do círculo.
        Parâmetro: r - o raio do círculo (int/float)
        Retorna a área (float)
        """

    # Fórmula área
    area = math.pi * r ** 2
    # Retorna a área do círculo
    # Outro comentário
    return area



""" Quando importado, o código abaixo não roda
"""

if __name__ == '__main__':
    raio = 2
    result = area_circle(raio)
    # Exemplo de formatação de output com float e duas casas decimais usando format
    print(f'A área é: {result:.2f}')
    outro_exemplo_comentado()

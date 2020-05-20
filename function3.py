""" Exemplo de função com dois parâmetros
"""


def soma(a, b):
    print('A soma é: ', a + b)


def soma_formatada(a, b):
    print(f'A soma é: {a + b:.2f}')


def multi(a, b):
    print(f'a multiplicação é : {a * b}')


if __name__ == '__main__':
    x = 10.5874
    y = 10.8787
    soma(x, y)
    soma_formatada(x, y)
    multi(16, 16)

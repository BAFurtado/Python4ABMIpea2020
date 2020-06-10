

def tabuada(num):
    """ Programa que retorna a tabuada impressa de um número 'num'
    """
    for i in range(1, 11):
        # exemplo da f'string'
        # a variável que se altera vai entre chaves
        print(f'{num} x {i} = {num * i}')


if __name__ == '__main__':
    n = int(input('qual valor?'))
    tabuada(n)

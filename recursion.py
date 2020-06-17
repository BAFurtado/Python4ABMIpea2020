""" From Think Python Allen Dowley """

import time


def countdown(n):
    # O primeiro valor de n é 10.
    # O segundo valor é 9, referente a 10 - 1
    if n <= 0:
        print('Lançamento !!!')
    else:
        # Imprime o 10
        print(n)
        # time.sleep(.25)
        return countdown(n - 1)
    # Quando ele for menor ou igual a zero, ele entra nessa linha,
    # não tem nada aqui, termina a função!


if __name__ == '__main__':
    m = 10
    countdown(m)

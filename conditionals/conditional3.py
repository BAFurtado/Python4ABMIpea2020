""" Learning about conditionals
    Pay attention to the DOIS PONTOS after the condition
    Note else is different from elif
    """

import random
import sys


def guessing():
    # Inicia um contador
    count = 0
    # Sorteia um numero entre 0 e 100. Guarda na variável "draw"
    draw = random.randint(0, 100)
    while True:
        guess = int(input('Entre um número entre 0 e 100: '))
        count += 1
        if guess > draw:
            print('Seu palpite é maior do que o valor sorteado')
        elif guess == draw:
            print('Congratulations, you got it')
            print('It took you {} tries'.format(count))
            sys.exit()
        else:
            print('Seu palpite é menor do que o valor sorteado')


if __name__ == '__main__':
    guessing()

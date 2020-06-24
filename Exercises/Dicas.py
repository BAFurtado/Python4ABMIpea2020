""" Algumas dicas referentes aos exercícios
"""

# Clone Paulo's repository from: https://github.com/pauloeam/programapython
# Clone https://github.com/RicardoWannerGodoy/Python
# Clone https://github.com/douglasmarcelinodossantos/Douglas_lista1_Python
import random
from string import ascii_letters as letters
from string import ascii_lowercase, ascii_uppercase


def manipulate_letters_easily():
    vogais = 'aeiou'
    vogais_u = vogais.upper()
    print(vogais[0])
    print(vogais_u[-1])
    print(letters)
    print(ascii_uppercase)
    teste1 = 'a'
    teste2 = '6'
    print(f"{teste1} is a string: {teste1.isalpha()}")
    print(f"{teste2} is a string: {teste2.isalpha()}")


# Três jeitos de contar ao reverso a lista
# Utilize dois for

def reduced_list1(n=4):
    for i in range(4):
        print(i)
    for i in range(4):
        print(n - i)


def reduced_list2(n=4):
    for i in range(n + 1):
        print(i)
    for i in reversed(range(n)):
        print(i)


def funcao_quest_10 (dicionario):
    # Change for a random value
    # starter = dicionario[random.choice(list(dicionario))]
    # replace maximo and minimo
    maximo = 0
    minimo = 0

    for each in dicionario:
        if dicionario[each] > maximo:
            maximo = dicionario[each]
        # Change for if
        # Change for <=
        if dicionario[each] <= minimo:

            minimo = dicionario[each]

    print("O valor mínimo da função seria:", minimo)
    print("O valor máximo da função seria:", maximo)


dic_quest10 = {'a': 15, 'b': 1, 'x': 4, 'y': 3, 'u': 15, 'e': 20, 'f': 12, 'b': 51, 'g': 7, 'z': 23}
funcao_quest_10(dic_quest10)


if __name__ == '__main__':
    manipulate_letters_easily()
    # reduced_list1()
    # reduced_list2(4)


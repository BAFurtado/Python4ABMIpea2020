""" Algumas dicas referentes aos exercícios
"""

# Clone Paulo's repository from: https://github.com/pauloeam/programapython
# Clone https://github.com/RicardoWannerGodoy/Python
# Clone https://github.com/douglasmarcelinodossantos/Douglas_lista1_Python
import random
from string import ascii_letters as letters
from string import ascii_lowercase, ascii_uppercase

# DICAS II. Novas correções ########################################################################################

# 1. Façam sempre FUNÇÕES. Fica reutilizável. É o jeito certo de lidar com a memória.
# Para checar se KEY está presente em um dicionário


# def function1():
#     pass


a = {'a': 1, 'b': 2}
'a' in a

# 2. Observem as informações da PyCharm sobre PEP (dois espaços antes de uma função, por exemplo).
# O código fica mais fácil de ler.

# 3. Não se esqueçam de usar o '__main__'... também fica reutilizável o código depois.

# if __name__ == '__main__':
#     function1()

# 4. Bem legal a resolução do Diego do exercício 14. Neste folder

# 5. Tinha um exercício que repete a mesma linha 16 vezes. Seria melhor utilizar um LOOP

for i in range(16):
    print(i)

# 6. Dois alunos usaram a função built-in max, min
# max(d.values())
# d = {'a': 1, 'z': 200}

# 7. Vários usaram f-string. Ótimo!

dicionario = {'a': 5, 'b': 10, 'e': 15, 'c': 20, 'i': 25, 'd': 30, 'o': 35, 'f': 40, 'u': 45, 'g': 50}
print(f'{2 * 8}')
# 8. Teve colega que usou Ipython. É uma boa estrutura para demonstrar código, resultado, código, resultado.


# 9. Teve função com bons nomes: "def bombril(utilidades):"

# 10. Teve colega também que orientou bem o usuário, com prints bastante ilustrativos...
def max_min_valor(dicionario):
    print(f'O valor máximo do dicionário é: {max(dicionario.values())}')



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
    starter = dicionario[random.choice(list(dicionario))]
    # replace maximo and minimo
    maximo = starter
    minimo = starter

    for each in dicionario:
        if dicionario[each] > maximo:
            maximo = dicionario[each]
        # Change for if
        # Change for <=
        if dicionario[each] < minimo:
            minimo = dicionario[each]

    print("O valor mínimo da função seria:", minimo)
    print("O valor máximo da função seria:", maximo)





if __name__ == '__main__':
    # manipulate_letters_easily()
    # reduced_list1()
    # reduced_list2(4)
    dic_quest10 = {'a': 1500, 'b': 10, 'x': -4, 'y': 3, 'u': -15, 'e': 200, 'f': 12, 'bb': 51, 'g': 7, 'z': 23}
    funcao_quest_10(dic_quest10)


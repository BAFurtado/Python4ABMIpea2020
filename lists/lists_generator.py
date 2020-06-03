import random


def generate():
    l = list()
    for i in range(9):
        l.append(random.randint(0, 10))
    return l


def media(lst):
    """ Recebe uma lista, calcula e retorna a média
    """
    return sum(lst)/len(lst)


def mediana(lst):
    """ Recebe uma lista, calcula a mediana e retorna o valor
    """
    lst.sort()
    indice_meio = int(len(lst)/2)
    return lst[indice_meio]



if __name__ == '__main__':
    a = generate()
    print(a)
    result = media(a)
    print(result)
    valor_mediana = mediana(a)
    print('O valor da mediana é ', valor_mediana)
    # print(a)
    # #
    # x = a.pop()
    # print(x)
    # print('Tamanho da lista ', len(a))
    # print(a.pop())
    # #
    # print('Novo tamanho da lista ', len(a))
    # #
    # for i in range(len(a)):
    #     print(a[i])

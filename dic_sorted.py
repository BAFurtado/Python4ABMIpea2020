""" Exemplo de sorted histogramas usando dicionários.
    Adaptado de Think Python. Chapter 11

"""
from lists import lists_generator


def histogram(data):
    # Calcula a frequência de ocorrência de cada chave
    d = dict()
    for each in data:
        d[each] = d.get(each, 0) + 1
    return d


def print_sorted(d):
    # Ordena o dicionário de acordo com a ordem alfabética
    # das keys
    for key in sorted(d):
        print(key, d[key])


if __name__ == '__main__':
    string1 = 'paralelepipedo'
    d1 = histogram(string1)
    print(string1)
    print_sorted(d1)
    print('')
    d2 = histogram(lists_generator.generate())
    print('lista aleatória')
    print_sorted(d2)

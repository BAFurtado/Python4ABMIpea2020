""" Exemplo de histogramas usando dicionários.
    Adaptado de Think Python. Chapter 11

"""
from lists import lists_generator

print('Introducing dictionary method .get(key, default values')
print(dict().get)
print('')

""" To illustrate the process, try to add a value to a key that does not exist.
    e = dict() 
    e['nokey'] = e['nokey'] + 1
    What happens?
    """


def histogram(data):
    d = dict()
    for each in data:
        # Ação: se a key já existe, adiciona 1. Senão: entra com o default 0. E adiciona o 1. O primeiro elemento.
        d[each] = d.get(each, 0) + 1
    return d


if __name__ == '__main__':
    # string1 = 'anticonstitucionalissimamente'
    # d1 = histogram(string1)
    # print(string1)
    # print(d1)
    print('')
    d2 = histogram(lists_generator.generate())
    print('lista aleatória')
    print(d2)
    # Introduce OPTIONAL PARAMETER IN FUNCTIONS...

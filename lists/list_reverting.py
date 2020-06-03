""" Demonstrating how to reverse a sentence by hand
    Try using the list method l.reverse()
"""


def reversing(name):
    b = list()
    for i in name:
        b.append(i)

    c = list()
    for i in range(len(b)):
        c.append(b.pop())

    resultado = ''.join(c)
    print(resultado)
    return resultado


if __name__ == '__main__':
    sentence = 'Godoy arrasou hoje...'
    sentence_revertida = reversing(sentence)
    reversing(sentence_revertida)


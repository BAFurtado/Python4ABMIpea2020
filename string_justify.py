

def right_justify(s):
    tamanho = len(s)
    print(" " * (70 - tamanho), s)


if __name__ == '__main__':
    palavra = 'anticonstitucionalissimamente'
    right_justify(palavra)
    palavra2 = 'inconstitucional'
    right_justify(palavra2)

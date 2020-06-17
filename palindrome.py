""" PseudoCódigo - pseudocode é o código descrito em palavras

"""

def primeira_letra(palavra):
    return palavra[0]


def ultima_letra(palavra):
    return palavra[-1]


def meio(palavra):
    return palavra[1:-1]


def main(palavra):
    palavra = str(palavra)
    if len(palavra) < 2:
        return True
    # o símbolo != é o operador lógico de diferença,
    # em contraste ao == que é de comparação
    if primeira_letra(palavra) != ultima_letra(palavra):
        return False
    else:
        return main(meio(palavra))


if __name__ == '__main__':
    # ARARA -- pode ser escrita de trás para frente que é a mesma palavra
    p1 = 'jaca'
    p2 = 'kadidja'
    p3 = 'ARARA'
    p4 = 1010101001010101
    p5 = 'NATAN'
    p6 = 'illmimlli'
    print(main(p6))



def paralelepipedo(base, altura, comprimento):
    return base * altura * comprimento


if __name__ == '__main__':
    b = .5
    h = .34
    c = 7.12
    print(paralelepipedo(b, h, c))
    print(paralelepipedo(b, b, b))
    print(paralelepipedo(1, 1, 1))
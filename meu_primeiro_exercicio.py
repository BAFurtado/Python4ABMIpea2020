

""" Primeiro exercício de função
    Fazer a função da área do triângulo, cuja
    fórmula é: base x altura / 2
    """


def area_triangulo(base, altura):
    area = base * altura / 2
    return area


if __name__ == '__main__':
    b = 2.75
    h = 3
    result = area_triangulo(b, h)
    print(result)


# Parâmetros. Return


def area_circle(raio):
    area = 3.14159 * raio ** 2
    print(area)
    return area


if __name__ == '__main__':
    raio = 10
    result = area_circle(raio)
    print(f'A área é: {result:.3f}')

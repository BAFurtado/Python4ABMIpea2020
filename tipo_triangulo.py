

def check_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        print('Seu triângulo é equilátero')
    elif (lado1 == lado2) or (lado2 == lado3) or (lado1 == lado3):
        print('Seu triângulo é isósceles')
    else:
        print('Seu triângulo é escaleno')


if __name__ == '__main__':
    a = 3
    b = 5
    c = 3
    # Input os tamanhos dos três lados do triângulo.
    # Descubra se é equilatero, isósceles ou escaleno.
    # Equilatero: 3 lados iguais, Isósceles 2, ou escaleno
    check_triangulo(a, b, c)



def conversor(valor, celsius='celsius'):
    # Exemplo de parâmetro opcional.
    # Basta incluir um "igual" no parenteses e o valor padrão
    # Se o parametro não for fornecido, ele utiliza o padrão
    # Isolar o C ou o F de cada lado da equação
    if celsius == 'celsius':
        f = valor
        # o Paulo Martins vai conferir a equação e as contas
        c = f * 1.8 + 32
        print(f'O valor {f} em fahrenheit é equivalente a {c} em celsius')
    else:
        c = valor
        f = 9 * c/5 + 32
        print(f'O valor {c} em fahrenheit é equivalente a {f} em celsius')


if __name__ == '__main__':
    conversor(100)
    conversor(0)
    conversor(32, 'fahrenheit')
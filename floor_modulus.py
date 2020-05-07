""" Função para converter minutos em horas e minutos
    Exemplifica floor division and modulus
    """


def hour_converter(minutes):
    # função de conversão
    h = minutes // 60
    m = minutes % 60
    print('{} horas e {} minutos'.format(h, m))


if __name__ == '__main__':
    min = 4400
    hour_converter(min)

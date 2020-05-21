"""
O usuário entra com um número de minutos e tem como retorno o número de horas e minutos resultantes
"""

entrada = int(input('Por favor, digite o numero de minutos: '))

horas = entrada // 60
minutos = entrada % 60

print(f'{entrada} minutos são {horas} horas e {minutos} minutos.')


import random


x = random.randint(0, 1000)

# if MAIS condição MAIS dois pontos
# elif MAIS condição MAIS dois pontos
# else não precisa de condição, são todos os outros casos
# então o programa continua da proxima linha não INDENTADA!

if x > 500:
    print('maior que 500')
elif x > 300:
    print('ele é menor que 500 e maior que 300')
elif x > 200:
    print('o valor é maior que duas centenas e menor que 3 centenas')
else:
    print('menor que 200')

print('o valor de fato do x é: ', x)
print('este é a continuidade do programa. depois de rodar os ifs, ele pula para a proxima linha não indentada')
print('print extra, x /1000', x / 1000)

print('execute selection in console ALT+SHIFT+E')
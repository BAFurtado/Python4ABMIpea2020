#Exercício 14


def contador(texto):

    lista_contada = []

    for caractere in "abcdefghijklmnopqrstuvwxyz":
        lista_contada.append(texto.lower().count(caractere))
    return tuple(lista_contada)

frase = input("Digite uma frase que iremos verificar se esta contém todas as letras do alfabeto! (não utilize acentos ou caracteres especiais!): ")
print('Sua frase é: \n',frase)
totais = contador(frase)
if 0 in totais:
    print ("Own, nem todas as letras do alfabeto constam no seu texto! Tente melhorar!")
else:
    print ("Que feito! Seu texto contém ao menos uma letra de cada uma do alfabeto. Parabéns!")





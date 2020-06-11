""" Building a simple dictionary """


""" Para guardar. Lembrar da diferença na hora do loop entre
    for i in :
    for cada_elemento in a:
   ...:     print(cada_elemento)
    
    e for i in range(len()):
    for cada_elemento in range(len(a)):
   ...:     print(cada_elemento)
    """

from collections import defaultdict

my_dict = defaultdict(list)

# SAME size lists.
NAMES = ['Alan', 'Bruno', 'Diego', "Douglas"]
AGES = [27, 38, 34, 37]
BIRTHDAYS = ['24-maio', '31-out', '14-julho', '1-marco']
EMPRESA = ['UFRGS', 'MIN_CIDADANIA', 'CGU', 'BB']


for i in range(len(NAMES)):
    for details in [AGES, BIRTHDAYS, EMPRESA]:
        my_dict[NAMES[i]].append(details[i])
#
# PARA CADA CHAVE NAS CHAVES DO MEU DICIONARIO
for key in my_dict.keys():
    # IMPRIMA A CHAVE E O VALOR DAQUELA CHAVE
    print(key, my_dict[key])
#
total_idade = 0
num_pessoas = len(my_dict)
for key in my_dict:
    # Pegar o primeiro elemento -- código 0 -- da lista correspondente aquela chave
    total_idade += my_dict[key][0]
print(f'a média de idades dos funcionário é {total_idade/num_pessoas}')
#

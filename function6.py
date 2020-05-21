# Importe todas as funções de dentro de function3.
# Acesse-as por meio de ponto: exemplo function3.soma()
import function2
import function3
import function5ab

function2.soma()
retorno = function3.soma(3, 3)
print(retorno)

function5ab.area_circle(10)
function5ab.area_circle(100)

# # Importe somente a função print_sentences do módulo function1
# # Acesse usando o alias/apelido ps
from function1 import print_sentences as ps


# # EXISTE A FUNÇÃO SOMA TANTO NO ARQUIVO FUNCTION2, FUNCTION3
# # Importe da function2 e use pelo nome direto soma()
from function2 import soma
from function5b import area_circle


if __name__ == '__main__':
    ps()
    soma()
    function3.soma(5, 6)
    print(area_circle(5))

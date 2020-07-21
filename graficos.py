""" Rápida demonstração gráficos
"""


# Sempre use a linha abaixo. É convenção Python
import matplotlib.pyplot as plt
import numpy as np

# Gerando dados aleatórios para trabalhar
x = np.random.randn(10000)

# 100 é o número de bins do histograma
plt.hist(x, bins=100, color='green')

# Note que aceita comandos tipo LaTeX -- entre símbolo dollar ($)
plt.title('Normal distribution with $t_0=0, x^2=32, \sigma=1$')
plt.savefig('meu_primeiro_histograma.png')
plt.show()


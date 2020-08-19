import matplotlib.pyplot as plt
import pandas as pd

p_eam = pd.read_csv('/Correcoes_Alunos/pauloeam/csv_cli.csv')
p_eam.drop(p_eam.columns[0], axis=1, inplace=True)
p_eam = p_eam.rename(columns={'Saldo Clientes Inicial': 'saldo_inicial', 'Saldo Clientes Final': 'saldo_final',
                              'Satisfação Clientes Inicial': 'satis_inicial',
                              'Satisfação Clientes Final': 'satis_final'})


# Exemplo como graficos.py
plt.hist(p_eam.saldo_inicial, 20, color='red', alpha=.8)
plt.show()
plt.hist(p_eam.saldo_final, 20, color='blue', alpha=.8)
plt.show()

# Exemplo direto do pandas
p_eam.hist()
plt.show()

ps = pd.read_csv('/Correcoes_Alunos/PauloSavio/arquivo1.csv',
                 sep=';', header=None)

satis, saldo, custo = list(), list(), list()
for i in range(len(ps)):
    if i % 3 == 0:
        print(i)
        satis.append(ps.loc[i, 1])
    elif (i - 1) % 3 == 0:
        print(i - 1)
        saldo.append(ps.loc[i, 1])
    elif (i - 2) % 3 == 0:
        print(i - 2)
        custo.append(ps.loc[i, 1])

plt.hist(satis, alpha=.2, color='red', bins=20)
plt.show()

plt.hist(custo, alpha=.2, color='blue', bins=20)
plt.show()

plt.hist(saldo, alpha=.2, color='green')
plt.show()

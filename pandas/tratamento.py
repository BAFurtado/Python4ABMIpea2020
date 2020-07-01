import numpy as np
import pandas as pd
import time

''' Limpeza da base 
    Escolhas feitas 
    '''

# Ler o arquivo
d = pd.read_csv('alugueis.csv', sep=';')
# Lista as cinco primeiras linhas da base
d.head()
d.columns
d.describe()
d.price.describe()
d.util.describe()
d.info()

# Processo inicial
print('Tamanho base original: {}'.format(len(d)))
print('Número colunas: {}'.format(len(d.columns)))

# Acessando colunas:
print(d.n_rooms.head())
print(d['n_rooms'].head())

# Changing alternated base
l = d.copy()

# Mostrando média e desvio
l.price.mean()
l.price.std()

print('Extracting ten largest Aluguel values')
l.price.nlargest(10)
l.price.nlargest(10).index
print(f'{l.loc[7122].price:,.0f}')
# Modificando a base
# Nós excluímos os 10 imóveis mais caros da base
# Estou escolhendo todas as linhas (todas as observações), que tem os 10 maiores valores para a coluna price
# Na sequencia, depois da virgula, eu nomeio a coluna e depois da igualdade o novo valor
# base.loc[condition, coluna] = novo_valor
l.loc[l.price.nlargest(10).index, 'price'] = np.nan

l.price.quantile(.25)
print('Trazendo mediana dos aluguéis para R$ {:.2f}'.format(l.price.quantile(.5)))

# Modificando a base novamente
print('Excluding values of sales above one standard deviation of nearly 124 million')
# Essa linha exclui 3.79% da minha base
# Podemos utilizar sum(l.price.isna()) para verificar o número de missing (na) valores na base
print(f'Numero de valores de aluguel com missing depois do ajuste para valores acima do desvio-padrão foi {sum(l.price.isna())}')
l.loc[l.price > l.price.std(), 'price'] = np.nan

# Python funções gerais/globais max(), sum(), len(), min()

# Modificando a base novamente, com ATRIBUIÇÃO de valor missing para a coluna 'util'
print('Excluindo áreas com valores 1')
l.loc[l['util'] == 1.0, 'util'] = np.nan
l.loc[l['util'] <= 8, 'util'] = np.nan

print('Excluding áreas below 7 sq meters')
l.loc[l['util'] < l['util'].quantile(.06), 'util'] = np.nan
l.loc[l['util'] < l['util'].quantile(.025), 'util'] = np.nan

# Renomeando coluna
# columns = {'valor_antigo': 'valor_novo'}
l = l.rename(columns={'neighborhood': 'bairro', 'expenses': 'condominio', 'parking': 'vagas'})

# Bairros diferentes
l.bairro.unique()

# Imóveis por bairro
l.bairro.value_counts().head(20)

print('Metade dos {} bairros tem até {} observações'.format(len(l.bairro.value_counts()),
                                                            l.bairro.value_counts().quantile(.5)))

# Retrato do Guará!
l.loc[l.bairro == 'Asa Sul', :].median()

# Generalizando para os 10 primeiros bairros
# Number formatting
pd.options.display.float_format = '{:,.2f}'.format
for b in l.bairro.value_counts().head(10).index:
    print(f'Bairro {b} __________________________')
    print(l.loc[l.bairro == b, :].mean())
    time.sleep(10)

# Groupby
bairros = l.groupby('bairro').agg('mean')
bairros.head(10)

bairros = l.groupby('bairro').agg(['mean', 'count'])

l.to_csv('alugueis_copia.csv', sep=';', index=False)


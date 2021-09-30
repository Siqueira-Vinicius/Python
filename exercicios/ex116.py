# importar panda
import numpy as np
# importar metodos de tabela
from pandas import Series, DataFrame
# gerar uma array(uma lista que é uma tupla)
dados = np.arange(6)
linha = ['linha1', 'linha2', 'linha3', 'linha4', 'linha5', 'linha6']
coluna = ['coluna1', 'coluna2', 'coluna3']
# indexar(numerar) o array
serie = Series(dados, index=linha)
print(serie)
print('\n')
# gerar sempre os mesmos valores aleatorios
np.random.seed(25)
# gerar 18 valores aleatorios na configuração 6 linhas e 3 colunas ,
# com as linhas denominadas com os nomes da lista 'linha' , e as colunas com os nomes da lsita 'colunas'
df = DataFrame(np.random.rand(18).reshape((6, 3)), index=linha, columns= coluna)
print(df)
print('\n')
# localizar elemento do dataframe
r = df.loc[['linha5', 'linha6'], ['coluna3']]
print(r)
print('\n')
# fatiar elemento do dataframe
fat = df.loc['linha1':'linha4']
print(fat)

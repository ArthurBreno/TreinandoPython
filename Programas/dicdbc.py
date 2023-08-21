mport pandas as pd
import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import doex

#----------DIC--------------------------------------------------------
data = pd.read_csv("exemplo_dic.csv")
print(data.size)
#construir lista
#definir numero de repetições...
repeticoes = 1
for i in range(0, data.size):
    if data['Racao'][i + 1] == data['Racao'][i]:
        repeticoes = repeticoes + 1
    else:
        break
print(repeticoes)
#numero de repetições deifnido
numeroTratamentos = int((data.size/2)/repeticoes)
lista = []
for i in range(0, numeroTratamentos):
    lista.append([])
for i in range(0, numeroTratamentos):
    for ii in range(0, repeticoes):
        lista[i].append(0)
iteradorRepecoes = 0
iteradorTratamentos = 0
contador = 0
print(lista)
while True:
    print("ITERA", contador)
    lista[iteradorTratamentos][iteradorRepecoes] = data['Peso'][contador]
    iteradorRepecoes = iteradorRepecoes + 1
    if contador > 1 and iteradorRepecoes == repeticoes:
        iteradorTratamentos = iteradorTratamentos + 1
        iteradorRepecoes = 0
    if contador > ((data.size/2)-2):
        break
    else:
        contador = contador + 1
#--------LISTA CONSTRUIDA---------------
exp = doex.CompletelyRandomizedDesign(lista[0], lista[1], lista[2], lista[3])

#---------------------------------------------------------------------------------------------
segundaLista = []
for i in range(0, int(data.size/2)):
    segundaLista.append(data['Peso'][i])
print(segundaLista)
print(len(segundaLista))
df = pd.DataFrame({'Peso': segundaLista, 'Racao': np.repeat(['a', 'b', 'c', 'd'], repeats=6)})

tukey = pairwise_tukeyhsd(endog=df['Peso'],
                          groups=df['Racao'],
                          alpha=0.05)
print(tukey)

#---------------------------DBC---------------------------------------------------------------------------------
data = pd.read_csv("exemplo_dbc.csv")
print(data.size)

#construir lista
#definir numero de repetições...
repeticoes = 1
for i in range(0, data.size):
    if data['tratamentos'][i + 1] == data['tratamentos'][i]:
        repeticoes = repeticoes + 1
    else:
        break
print(repeticoes)
#numero de repetições deifnido
numeroTratamentos = int((data.size/3)/repeticoes)
lista = []
for i in range(0, numeroTratamentos):
    lista.append([])
for i in range(0, numeroTratamentos):
    for ii in range(0, repeticoes):
        lista[i].append(0)
iteradorRepecoes = 0
iteradorTratamentos = 0
contador = 0
print(lista)
while True:
    print("ITERA", contador)
    lista[iteradorTratamentos][iteradorRepecoes] = data['resultados'][contador]
    iteradorRepecoes = iteradorRepecoes + 1
    if contador > 1 and iteradorRepecoes == repeticoes:
        iteradorTratamentos = iteradorTratamentos + 1
        iteradorRepecoes = 0
    if contador > ((data.size/3)-2):
        break
    else:
        contador = contador + 1
#--------LISTA CONSTRUIDA---------------

exp = doex.RandomizedCompleteBlockDesign(lista)

#---------------------------------------------------------------------------------------------
segundaLista = []
for i in range(0, int(data.size/3)):
    segundaLista.append(data['resultados'][i])
print(segundaLista)
print(len(segundaLista))
df = pd.DataFrame({'resultados': segundaLista, 'tratamentos': np.repeat(['a', 'b', 'c', 'd', 'e'], repeats=4)})

tukey = pairwise_tukeyhsd(endog=df['resultados'],
                          groups=df['tratamentos'],
                          alpha=0.05)
print(tukey)
# ---------------------------------------------------------------------------------------------------------
# fatorial bdc
data = pd.read_csv("exemplo_dbc_fatorial.csv")
print(data)
model = ols('resultado ~ C(bloco) + C(tratamento1)*C(tratamento2)', data=data).fit()
result = sm.stats.anova_lm(model, type=2)
print(result)

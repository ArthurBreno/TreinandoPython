import pandas as pd
from tabulate import tabulate
data = pd.read_csv("exemplo_dbc_parcela_subdividida_interacao.csv")
print(data)

parcela = ['A1', 'A2', 'A3', 'A4']
subparcelas = ['B1', 'B2', 'B3', 'B4']
repeticoes = 4
numeroUnidade = len(parcela)*len(subparcelas)*repeticoes
c_correcao = 0
#------------------------------------------------------------
# calculo C
somatoria = 0
for i in range(0, numeroUnidade):
    somatoria = somatoria + data['resultado'][i]
somatoria = somatoria * somatoria
somatoria = somatoria / (len(parcela)*len(subparcelas)*repeticoes)
c_correcao = somatoria
#----------------------------------------------------------------
# calculo SQ TOTAL
sq_total = 0
for i in range(0, numeroUnidade):
    sq_total = sq_total + (data['resultado'][i])**2
sq_total = sq_total - c_correcao
print("sq total = ", sq_total)
#------------------------------------------------------------------
# calculo sq de bloco
sq_blocos = 0
listaSqBloco = []
countTemp = 0
#realizar a somatoria para cada bloco
for i in range(0, repeticoes):
    countTemp = i
    listaSqBloco.append([])
    for ii in range(i, numeroUnidade, repeticoes):
        listaSqBloco[i].append(data['resultado'][countTemp])
        countTemp = countTemp + repeticoes
print(listaSqBloco)
listaQuadradoBlocos = []
countTemp = 0
for i in range(0, len(listaSqBloco)):
    for ii in range(0, len(listaSqBloco[0])):
        countTemp = countTemp + listaSqBloco[i][ii]
        if ii == len(listaSqBloco[0]) - 1:
            countTemp = countTemp**2
            listaQuadradoBlocos.append(countTemp)
            countTemp = 0
countTemp = 0
# print(listaQuadradoBlocos)
for i in range(0, len(listaQuadradoBlocos)):
    countTemp = countTemp + listaQuadradoBlocos[i]
sq_blocos = (countTemp/(len(parcela)*len(subparcelas))) - c_correcao
print("sq blocos = ", sq_blocos)
#---------------------------------------------------------------------------
# calculo sq de parcelas
listaSqlParcela = listaSqBloco
print(listaSqlParcela)
listaSqQuadradoParcela = []
listaTemp = []
countTemp = 0
countRepeti = 0
for i in range(0, len(listaSqlParcela)):
    for ii in range(0, len(listaSqlParcela[0])):
        countTemp = countTemp + 1
        countRepeti = listaSqlParcela[i][ii] + countRepeti
        listaTemp.append(listaSqlParcela[i][ii])
        if countTemp == len(subparcelas):
            countRepeti = countRepeti**2
            listaSqQuadradoParcela.append(countRepeti)
            countRepeti = 0
            countTemp = 0
            listaTemp = []
print(listaSqQuadradoParcela)
countTemp = 0
for i in range(0, len(listaSqQuadradoParcela)):
    countTemp = countTemp + listaSqQuadradoParcela[i]
sq_parcelas = (countTemp/len(subparcelas)) - c_correcao
print('sq parcelas = ', sq_parcelas)
# ---------------------------------------------------------------------------
#calculo sq tratamento 01
listaSQtratamento01 = []
countTemp = 0
#sq tratamento01
for i in range(0, len(parcela)):
    for ii in range(0, numeroUnidade):
        if parcela[i] == data['parcela'][ii]:
            countTemp = countTemp + data['resultado'][ii]
    countTemp = countTemp**2
    listaSQtratamento01.append(countTemp)
    countTemp = 0
print(listaSQtratamento01)
countTemp = 0
for i in range(0, len(listaSQtratamento01)):
    countTemp = countTemp + listaSQtratamento01[i]
sq_tratamento01 = (countTemp/(len(subparcelas)*repeticoes)) - c_correcao
print('sq tratamento01 = ', sq_tratamento01)
# ---------------------------------------------------------------------------
#calculo sq tratamento 01
listaSQtratamento02 = []
countTemp = 0
for i in range(0, len(subparcelas)):
    for ii in range(0, numeroUnidade):
        if subparcelas[i] == data['subparcela'][ii]:
            countTemp = countTemp + data['resultado'][ii]
    countTemp = countTemp**2
    listaSQtratamento02.append(countTemp)
    countTemp = 0
print(listaSQtratamento02)
countTemp = 0
for i in range(0, len(listaSQtratamento02)):
    countTemp = countTemp + listaSQtratamento02[i]
sq_tratamento02 = (countTemp/(len(parcela)*repeticoes)) - c_correcao
print('sq tratamento02 = ', sq_tratamento02)
# ---------------------------------------------------------------------------
#calculo sq tratamento da interação.....
listaSQinteracao = []
countTemp = 0
for i in range(0, len(parcela)*len(subparcelas)):
    for ii in range(0, repeticoes):
        countTemp = countTemp + listaSqBloco[ii][i]
    countTemp = countTemp**2
    listaSQinteracao.append(countTemp)
    countTemp = 0
print(listaSQinteracao)
countTemp = 0
for i in range(0, len(listaSQinteracao)):
    countTemp = countTemp + listaSQinteracao[i]
sq_iteracao = (countTemp/(repeticoes)) - c_correcao
sq_iteracaoCorrido = sq_iteracao - sq_tratamento01 - sq_tratamento02
print('sq iteracao = ', sq_iteracao)
# ---------------------------------------------------------------------------
# calculo SQ residuo A
sq_residuoA = sq_parcelas - sq_blocos - sq_tratamento01
print('sq residuo A', sq_residuoA)
# ---------------------------------------------------------------------------
# calculo SQ residuo B
sq_residuoB = sq_total - sq_parcelas - sq_tratamento02 - sq_iteracaoCorrido
print('sq residuo B', sq_residuoB)
# ---------------------------------------------------------------------------
# calculo dos graus de liberdade
gl_blocos = repeticoes - 1
gl_tratamento01 = len(parcela) - 1
gl_residuoA = gl_blocos * gl_tratamento01
gl_parcela = (len(parcela)*len(subparcelas)) - 1
gl_tratamento02 = len(subparcelas) - 1
gl_interacao = (len(parcela) - 1) * (len(subparcelas) - 1)
gl_residuoB = len(parcela) * (len(subparcelas) - 1) * (len(parcela) - 1)
gl_total = (repeticoes*len(parcela)*len(subparcelas)) - 1
# ---------------------------------------------------------------------------
# calculo dos quadrados medios
qm_blocos = sq_blocos/gl_blocos
qm_tratamento01 = sq_tratamento01/gl_tratamento01
qm_residuoA = sq_residuoA/gl_residuoA
qm_tratamento02 = sq_tratamento02/gl_tratamento02
qm_interacao = sq_iteracaoCorrido/gl_interacao
qm_residuoB = sq_residuoB/gl_residuoB
# ---------------------------------------------------------------------------
# F calculado
f_bloco = qm_blocos/qm_residuoA
f_tratamento01 = qm_tratamento01/qm_residuoA
f_tratamento02 = qm_tratamento02/qm_residuoB
f_interacao = qm_interacao/qm_residuoB

tabelaImprimir = [["BLOCOS", gl_blocos, sq_blocos, qm_blocos, f_bloco],
                  ["TRATAMENTO 01", gl_tratamento01, sq_tratamento01, qm_tratamento01, f_tratamento01],
                  ["RESIDUO A", gl_residuoA, sq_residuoA, qm_residuoA, "-"],
                  ["PARCELA", gl_parcela, sq_parcelas, "-", "-"],
                  ["TRATAMENTO 02", gl_tratamento02, sq_tratamento02, qm_tratamento02, f_tratamento02],
                  ["INTERAÇÃO AxB", gl_interacao, sq_iteracao, qm_interacao, f_interacao],
                  ["RESIDUO B", gl_residuoB, sq_residuoB, qm_residuoB, "-"],
                  ["TOTAL", gl_total, sq_total, "-", "-"]]

print(tabulate(tabelaImprimir, headers=["causa da variação", "G.L.", "S.Q.", "Q.M.", "F"]))

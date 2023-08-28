import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

tabela = pd.read_excel("IDROP.xlsx")
tabelaCUC = tabela.drop("CUD", axis=1)
tabelaCUD = tabela.drop("CUC", axis=1)

# df_max_scaled = tabela.copy()
# for column in df_max_scaled.columns:
#     df_max_scaled[column] = df_max_scaled[column] / df_max_scaled[column].abs().max()
# print(df_max_scaled.corr()[["CUD"]])
print("---------------------------")
print('CUC--- ----')
for column in tabelaCUC.columns:
    tabelaCUC[column] = tabelaCUC[column] / tabelaCUC[column].abs().max()
y = tabelaCUC["CUC"]
# #axis=0->eixo das linhas, axis=1-> eixo das colunas
x = tabelaCUC.drop("CUC", axis=1)
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, train_size=0.8, random_state=1)

modelo_regressaolinear = LinearRegression()
modelo_floresta = RandomForestRegressor()

modelo_regressaolinear.fit(x_treino, y_treino)
modelo_floresta.fit(x_treino, y_treino)

linear = modelo_regressaolinear.predict(x_teste)
floresta = modelo_floresta.predict(x_teste)
print(r2_score(y_teste, linear))
print(r2_score(y_teste, floresta))
print("--------------------------------------------")
print("CUD---------")
for column in tabelaCUD.columns:
    tabelaCUD[column] = tabelaCUD[column] / tabelaCUD[column].abs().max()
y = tabelaCUD["CUD"]
# #axis=0->eixo das linhas, axis=1-> eixo das colunas
x = tabelaCUD.drop("CUD", axis=1)
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, train_size=0.8, random_state=1)

modelo_regressaolinear = LinearRegression()
modelo_floresta = RandomForestRegressor()

modelo_regressaolinear.fit(x_treino, y_treino)
modelo_floresta.fit(x_treino, y_treino)

linear = modelo_regressaolinear.predict(x_teste)
floresta = modelo_floresta.predict(x_teste)

print(r2_score(y_teste, linear))
print(r2_score(y_teste, floresta))

# # Seaparar a base de dados em X e Y
# y = df_max_scaled["CUD"]
# # #axis=0->eixo das linhas, axis=1-> eixo das colunas
# x = df_max_scaled.drop("CUD", axis=1)
#
# x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, train_size=0.8, random_state=None)
#
# modelo_regressaolinear = LinearRegression()
# modelo_floresta = RandomForestRegressor()
#
# modelo_regressaolinear.fit(x_treino, y_treino)
# modelo_floresta.fit(x_treino, y_treino)





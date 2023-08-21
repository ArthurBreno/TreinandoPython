import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

tabela = pd.read_excel("acliveIDROPCUC.xlsx")
# print(tabela.info())
print(tabela.corr()[["CUC"]])

# Seaparar a base de dados em X e Y
y = tabela["CUC"]
# #axis=0->eixo das linhas, axis=1-> eixo das colunas
x = tabela.drop("CUC", axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, train_size=0.7, random_state=1)

modelo_regressaolinear = LinearRegression()
modelo_floresta = RandomForestRegressor()

modelo_regressaolinear.fit(x_treino, y_treino)
modelo_floresta.fit(x_treino, y_treino)

linear = modelo_regressaolinear.predict(x_teste)
floresta = modelo_floresta.predict(x_teste)

print(r2_score(y_teste, linear))
print(r2_score(y_teste, floresta))

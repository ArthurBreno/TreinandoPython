#https://www.pythonfordatascience.org/anova-python/
#https://doex.rohitsanjay.com/en/latest/examples.html#randomized-complete-block-design

import doex
import pandas as pd
import scipy.stats as stats
import researchpy as rp
import statsmodels.api as sm
from statsmodels.formula.api import ols
# oq caraio é df = dataFrame
#DIC
# df_dic = pd.read_csv('exemplo_dic.txt')

# def anova_table(aov):
#      aov['mean_sq'] = aov[:]['sum_sq']/aov[:]['df']
#
#      aov['eta_sq'] = aov[:-1]['sum_sq']/sum(aov['sum_sq'])
#
#      aov['omega_sq'] = (aov[:-1]['sum_sq']-(aov[:-1]['df']*aov['mean_sq'][-1]))/(sum(aov['sum_sq'])+aov['mean_sq'][-1])
#
#      cols = ['sum_sq', 'df', 'mean_sq', 'F', 'PR(>F)', 'eta_sq', 'omega_sq']
#      aov = aov[cols]
#      return aov
#
#
# model = ols('Peso ~ Racao', data=df_dic).fit()
# aov_table = sm.stats.anova_lm(model, typ=2)
# print(anova_table(aov_table))
# ---------------------------------------------------------------------------------------------------------------------------
#DBC
# exp = doex.RandomizedCompleteBlockDesign(
#     [
#         [60,50,65,40],
#         [70,80,75,90],
#         [100,90,85,75],
#         [90,110,95,105],
#         [120,105,140,95],
#     ]
# )

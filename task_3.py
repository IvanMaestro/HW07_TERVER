# Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.
# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут: 140, 155, 150, 130, 135


import numpy as np
import scipy.stats as stats

N_0 = 'Нет статистически значимых различий'
N_1 = 'Статистически значимые различия имеются'

x_0 = np.array([150, 160, 165, 145, 155])
x_10 = np.array([140, 155, 150, 130, 135])

test = stats.wilcoxon(x_0, x_10)
stat, p = test[0], test[1]

# print(test)

alpha = 0.05
if p > alpha:
    print(N_0)
else:
    print(N_1)
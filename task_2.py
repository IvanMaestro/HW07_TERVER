# Исследовалось влияние препарата на уровень давления пациентов.
# Сначала измерялось давление до приема препарата, потом через
# 10 минут и через 30 минут. Есть ли статистически значимые различия?
# 1е измерение до приема препарата: 150, 160, 165, 145, 155
# 2е измерение через 10 минут: 140, 155, 150, 130, 135
# 3е измерение через 30 минут: 130, 130, 120, 130, 125

import numpy as np
import scipy.stats as stats

N_0 = 'Нет статистически значимых различий'
N_1 = 'Статистически значимые различия имеются'

x_0 = np.array([150, 160, 165, 145, 155])
x_10 = np.array([140, 155, 150, 130, 135])
x_30 = np.array([130, 130, 120, 130, 125])

test = stats.friedmanchisquare(x_0, x_10, x_30)
stat, p = test[0], test[1]

# print(test)

alpha = 0.05
if p > alpha:
    print(N_0)
else:
    print(N_1)

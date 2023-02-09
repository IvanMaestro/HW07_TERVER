# Даны две независимые выборки. Не соблюдается условие нормальности
# x1 380,420, 290
# y1 140,360,200,900
# Сделайте вывод по результатам, полученным с помощью функции

import numpy as np
import scipy.stats as stats

N_0 = 'Нет статистически значимых различий'
N_1 = 'Статистически значимые различия имеются'


x1 = np.array([380, 420, 290])
y1 = np.array([140, 360, 200, 900])

test = stats.mannwhitneyu(x1, y1)
stat, p = test[0], test[1]

# print(test)

alpha = 0.05
if p > alpha:
    print(N_0)
else:
    print(N_1)

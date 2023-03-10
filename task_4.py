# Даны 3 группы учеников плавания.
# В 1 группе время на дистанцию 50 м составляют:
# 56, 60, 62, 55, 71, 67, 59, 58, 64, 67
# Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
# Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54
# Есть ли различия между группами?

import numpy as np
import scipy.stats as stats

N_0 = 'Нет статистически значимых различий'
N_1 = 'Статистически значимые различия имеются'

gr1 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
gr2 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
gr3 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

test = stats.kruskal(gr1, gr2, gr3)
stat, p = test[0], test[1]

# print(test)

alpha = 0.05
if p > alpha:
    print(N_0)
else:
    print(N_1)
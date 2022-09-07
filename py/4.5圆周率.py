# 近似公式
print('# 近似公式')
pi = 0
N = 100
for k in range(N):
    pi += 1 / pow(16, k) * \
          (4 / (8 * k + 1) - 2 / (8 * k + 4) -
           1 / (8 * k + 5) - 1 / (8 * k + 6))
print(pi)
# 蒙特卡罗方法
print('# 蒙特卡罗方法')
from random import random
from time import perf_counter
darts = 1000 *1000
hits = 0.0
start = perf_counter()
for i in range(darts):
    x,y = random(),random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits/darts)
print('pi为:{}'.format(pi))
print('运行时间为：{}'.format(perf_counter()-start))
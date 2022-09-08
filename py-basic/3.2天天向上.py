# 每天进步一点点
print('# 每天进步一点点')
dayfactor = eval(input('输入参数:'))
dayup = pow(1 + dayfactor, 365)
daydown = pow(1 - dayfactor, 365)
print("向上:{:.2f},向下:{:.2f}".format(dayup, daydown))
# 工作日的力量
print('# 工作日的力量')
dayup = 1
for i in range(365):
    if i % 7 in [0, 6]:
        dayup *= 1 - dayfactor
    else:
        dayup *= 1 + dayfactor
print('工作日的力量:{:.2f}'.format(dayup))

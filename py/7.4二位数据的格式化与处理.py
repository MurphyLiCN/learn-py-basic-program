# 二维列表 ls[row][column] 先行后列
# CSV逗号分隔值
# 读入处理
fo = open('/Users/murphy/学业/python/学习-程序设计/数据文件/7.4二维数据.csv')
ls = []
for line in fo:
    line = line.replace('\n', '')
    ls.append(line.split(','))
fo.close()

# %% 写入
ls = [['1', '2'], ['3', '4'], ['5', '6']]
f = open('/Users/murphy/学业/python/学习-程序设计/数据文件/7.4二维数据写入.csv', 'w')
for item in ls:
    f.write(','.join(item) + '\n')
f.close()
# %% 遍历
for row in ls:
    for column in row:
        print(column)

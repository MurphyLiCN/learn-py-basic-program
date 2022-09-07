# 接口定义：行进距离，转向方向（0左1右），转向角度，RGB色彩
# 自动化思维：数据与功能分离，数据驱动自动运行
# 接口化设计：格式化接口设计

# 基础准备
import turtle as t

t.title('自动轨迹绘制')
t.setup(800, 600, 0, 0)
t.pencolor('red')
t.pensize(5)

# 数据读取（二维数据）
datals = []
fpath = '/Users/murphy/学业/python/学习-程序设计/数据文件/自动轨迹绘制.txt'
f = open(fpath)
for line in f:
    line = line.replace('\n', '')
    datals.append(list(map(eval, line.split(','))))
f.close()

# 自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])

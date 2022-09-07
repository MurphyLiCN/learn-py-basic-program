# 理解与定义(IPO)
print('# 理解与定义(IPO)')

def fact(n, m=1, *b):
    s = 1
    for i in range(1, n + 1):
        s *= i
    for item in b:
        s *= item
    return s // m, n, m


# 调用
print('# 调用')
a = fact(10, 4, 1, 2, 3, 5)
print(a)

# 参数传递（必选，可选，可变）
print('# 参数传递（必选，可选，可变）')
a = fact(10, 4, 1, 2, 3, 5)
b = fact(m=5, n=10)
print(a, b)

# 返回值
print('# 返回值')
a, b, c = fact(2, 3, 4, 5, 6)
d = fact(2, 3, 4, 5, 6)
print(a, b, c, d)

# 局部变量与全局变量（global声明的基本类型 & 未被内部创建的组合类型）
print('# 局部变量与全局变量')


def fact_g(n, m=1, *b):
    global s
    for i in range(1, n + 1):
        s *= i
    for item in b:
        s *= item
    return s // m, n, m


s = 1
print(fact(10), s)
print(fact_g(10), s)


def func(a):
    ls = []
    ls.append(a)
    return


def func_g(a):
    ls.append(a)
    return


ls = ['F', 'f']
func('C')
print(ls)
func_g('C')
print(ls)

# lambda函数
f = lambda x, y: x + y
print(f(10,15))

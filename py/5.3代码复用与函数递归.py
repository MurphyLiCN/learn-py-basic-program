# 代码复用与模块化设计
print('# 代码复用与模块化设计')
# 函数递归（基例与链条）数学归纳法（假设我已经可以XX）
print('# 函数递归（基例+链条,函数+分枝）数学归纳法')
# 阶乘
print('# 阶乘')


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))

# 字符串反转
print('# 字符串反转')


def rvs(s):
    if s == '':
        return s
    else:
        return rvs(s[1:]) + s[0]


print('python123'[::-1])
print(rvs('python123'))

# 斐波那契数列
print('# 斐波那契数列')


def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


print(f(7))

# 汉诺塔问题
print('# 汉诺塔问题')


def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print('{}:{}->{}'.format(1, src, dst))
        count += 1
    else:
        hanoi(n - 1, src, mid, dst)
        print('{}:{}->{}'.format(n, src, dst))
        count += 1
        hanoi(n - 1, mid, dst, src)


count = 0
hanoi(4, 'A', 'B', 'C')
print(count)

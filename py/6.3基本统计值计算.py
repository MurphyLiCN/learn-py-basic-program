def get_num():
    nums = []
    in_num_str = input('请输入数字（回车退出）：')
    while in_num_str != '':
        nums.append(eval(in_num_str))
        in_num_str = input('请输入数字（回车退出）：')
    return nums


def mean(ls):
    s = 0.0
    for item in ls:
        s += item
    return s / len(ls)


def var(ls, mean):
    s_var = 0.0
    for item in ls:
        s_var += (item - mean) ** 2
    return pow(s_var / (len(ls) - 1), 0.5)


def median(ls):
    sorted(ls)
    size = len(ls)
    if size % 2 == 0:
        med = (ls[size // 2 - 1] + ls[size // 2]) / 2
    else:
        med = ls[size // 2]
    return med


ls = get_num()
print(ls, mean(ls), var(ls, mean(ls)), median(ls))

# 自顶向下（设计），自底向上（执行）
from random import random


# 1.分解任务
# 主函数
def main():
    print_intro()
    P_A, P_B, n = get_inputs()
    win_A, win_B = sim_n_games(n, P_B, P_B)
    print_summary(win_A, win_B)


# 2.小任务
# 打印介绍性信息
def print_intro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")


# 获取参数
def get_inputs():
    a = eval(input("请输入选手A的能力值(0-1): "))
    b = eval(input("请输入选手B的能力值(0-1): "))
    n = eval(input("模拟比赛的场次: "))
    return a, b, n


# 模拟n局
def sim_n_games(n, P_A, P_B):
    win_A, win_B = 0, 0
    for i in range(n):
        score_A, score_B = sim_one_game(P_A, P_B)
        if score_A > score_B:
            win_A += 1
        else:
            win_B += 1
    return win_A, win_B


# 输出
def print_summary(Win_A, Win_B):
    n = Win_A + Win_B
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(Win_A, Win_A / n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(Win_B, Win_B / n))


# 3.再细分
def sim_one_game(P_A, P_B):
    score_A, score_B = 0, 0
    serving = 'A'
    while not game_over(score_A, score_B):
        if serving == 'A':
            if random() < P_A:
                score_A += 1
            else:
                serving = 'B'
        else:
            if random() < P_B:
                score_B += 1
            else:
                serving = 'A'
    return score_A, score_B


def game_over(score_A, score_B):
    return score_A == 15 or score_B == 15


# 4.主程序
if __name__ == '__main__':
    main()

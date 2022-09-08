# 拆解任务，模块化，规则化
import turtle, time


# 绘制间隔
def draw_gap():
    turtle.penup()
    turtle.fd(5)


# 绘制一条线并转向
def draw_line(draw):
    draw_gap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    draw_gap()
    turtle.right(90)


# 绘制七条线
def draw_digit(digit):
    draw_line(True) if digit in [2, 3, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 3, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 6, 8] else draw_line(False)
    turtle.left(90)
    draw_line(True) if digit in [0, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else draw_line(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


# 绘制一段数
def draw_data(data):
    turtle.pencolor('red')
    for i in data:
        if i == '年':
            turtle.write('年', font=('Arial', 18, 'normal'))
            turtle.fd(40)
            turtle.pencolor('green')
        elif i == '月':
            turtle.write('月', font=('Arial', 18, 'normal'))
            turtle.fd(40)
            turtle.pencolor('blue')
        elif i == '日':
            turtle.write('日', font=('Arial', 18, 'normal'))
            turtle.fd(40)
        else:
            draw_digit(eval(i))


# 主程序
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    draw_data(time.strftime('%Y年%m月%d日', time.gmtime()))
    turtle.hideturtle()
    turtle.done()


main()

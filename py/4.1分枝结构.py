#单分枝
print('#单分枝')
guess = eval(input('请输入数字：'))
if  guess == 99:
    print('猜对了')

#二分枝
print('#二分枝')
if guess == 99:
    print('猜对了')
else:
    print('猜错了')

#紧凑二分枝(无法赋值）
print('#紧凑二分枝(无法赋值）')
print('猜{}了'.format('对' if guess == 99 else'错'))

#多分枝
print('#多分枝')
if guess > 90:
    print('>90')
elif guess > 60:
    print('>60')
else:
    print('haha')

#条件判断
print('#条件判断')
# > <= < <= == != and or not True False

#异常处理
print('#异常处理')
try:
    num = eval(input('输入一个数字：'))
except NameError:
    print('不是整数')
else:
    print('输入格式正确')
    print(num ** 2)
finally:
    print('结束')



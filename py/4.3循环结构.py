#遍历循环
print('#遍历循环')
for i in range(0,6,2):
    print(i)

for c in 'python123':
    print(c,end=',')

for item in [123,'py',456]:
    print(item)
#无限循环
print('#无限循环')
a = 3
while a > 0 :
    a -= 1
    print(a)

#保留字 break continue
print('#保留字 break continue')
for c in  'python':
    if c == 't':
        continue
    print(c,end='')
print('')

for c in  'python':
    if c == 't':
        break
    print(c,end='')
print('')

#循环嵌套,break仅跳出最内层循环
print('#循环嵌套,break仅跳出最内层循环')
s='python'
while s != '':
    for c in s:
        print(c,end='')
    s = s[:-1]
print('')

s='python'
while s != '':
    for c in s:
        if c=='t':
            break
        print(c,end='')
    s = s[:-1]
print('')

#else 如果没有遇到break就执行
print('#else 如果没有遇到break就执行')
for c in  'python':
    if c == 't':
        continue
    print(c,end='')
else:
    print('正常退出')

for c in  'python':
    if c == 't':
        break
    print(c,end='')
else:
    print('正常退出')



# 单行与多行
print('# 单行与多行')
print('c')
print('''cc
ccc''')
print('使用"表示引号')
# 索引与切片
print('# 索引与切片')
print('123456789'[0],
      '123456789'[1:3],
      '123456789'[2:-2],
      '123456789'[:3],
      '123456789'[1:8:2],
      '123456789'[::-1])
# 转义符\
print('# 转义符')
print('这里\b有个\n单引\r号\'')
# 操作符
print('# 操作符')
x = '123'
y = '456'
z = '123456'
print(x + y,
      x * 3,
      x in y,
      x in z)
# 处理函数
print('# 处理函数')
print(len('123'),
      str(1.23),
      str([1, 2, 3]),
      hex(123),
      oct(123),
      ord('1'),
      chr(49))
for i in range(12):
    print(chr(9800 + i), end=' ')
print('over')
# 方法
print('# 方法')
Str = '123,aBc.'
print(Str.lower(),
      Str.upper(),
      Str.split(','),
      Str.count('a'),
      Str.replace('a', 'aaaaaaa'),
      Str.center(20, '='),
      Str.strip('12c'),
      ','.join('12345'))
# 格式化
print('# 格式化')
print('{}:计算机{}的CPU占用率为{}%'.format('2018-10-10', 'c', 10), '\n',
      '{1}:计算机{0}的CPU占用率为{2}%'.format('2018-10-10', 'c', 10), '\n',
      '格式控制(序号:填充对齐宽度 千分位符 精度 类型){0:=^20,.2f}'.format(123456.789), '\n',
      '{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}'.format(425), '\n',
      '{0:e},{0:E},{0:f},{0:%}'.format(3.14)
      )

name = "Python语言程序设计课程"
print(name[0], name[2:-2], name[-1])

s = 'python'
print('{0:3}'.format(s))

# 整数,不同进制
print('# 整数,不同进制')
pow(2, 100)
print(1010, 0b1010, 0o1010, 0x1010)
# 浮点数,有不确定尾数,科学计数法
print('# 浮点数,有不确定尾数,科学计数法')
print(0.1 + 0.3,
      0.1 + 0.2,
      0.1 + 0.2 == 0.3,
      round(0.1 + 0.2, 1) == 0.3,
      4.3e-3,
      9.6E5)
# 复数
print('# 复数')
z = 1.23e-4 + 89j
print(z.real, z.imag)
# 数值运算操作符,二元操作符 x op= y
print('# 数值运算操作符,二元操作符 x op= y')
x = 10
y = 3
print(x + y,
      x - y,
      x * y,
      x ** y,
      x / y,
      x // y,
      x % y,
      +x,
      -y,
      )
x += y
print(x)
#运算函数
print('#运算函数')
print(abs(x),
      divmod(x,y),
      pow(3,99,1000),
      round(-10.123,2),
      min(1,2),
      int(123.8),
      int('123'),
      float('123.8'),
      complex(4))


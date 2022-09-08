# 文件的类型：文本文件（有统一编码，如UTF-8）与二进制文件
fname = '/Users/murphy/学业/python/学习-程序设计/数据文件/校歌.txt'

# 文件的打开与关闭（文件的存储状态与占用状态）：打开-操作-关闭
tf = open(fname, 'rt')
print(tf.readline())
tf.close()

tb = open(fname, 'rb')
print(tb.readline())
tb.close()
# 文件内容的读取
tf = open(fname, 'rt')
print(tf.read(10))
print(tf.readline(10))
print(tf.readlines(5))
tf.close()

# 遍历全文件
print('# 一次读入，统一处理')
fo = open(fname, 'r')
txt = fo.read()
# 文件处理代码
fo.close()

print('# 按数量读入，逐步处理')
fo = open(fname, 'r')
txt = fo.read(2)
while txt != '':
    # 文件处理代码
    txt = fo.read(2)
fo.close()

print('# 一次读入，逐行处理')
fo = open(fname, 'r')
for line in fo.readlines():
    print(line)
fo.close()

print('# 逐行读入，逐行处理')
fo = open(fname, 'r')
for line in fo:
    print(line)
fo.close()

# 数据的文件写入
print('# 数据的文件写入')
fo = open(fname, 'a+')
lines = ['法国', '中国', '美国']
fo.writelines(lines)
fo.seek(0)  # 指针位置
for line in fo:
    print(line)
fo.close()


# 集合类型的定义(多个不重复元素的无序组合）
print('# 集合类型的定义')
A = {'python', 123, ('python', 123)}
print(A)
B = set('pypy123')
print(B)
C = {'python', 123, 'python', 123}
print(C)

# 集合操作符(并|、差-、交&、补^、子集<、包含>)，增强操作符(|= -= &= ^=)
print('# 集合操作符(并|、差-、交&、补^、子集<、包含>）')
A = {'p', 'y', 123}
B = set('pypy123')
print(A, B)
print(A | B, A - B, A & B, A ^ B)

# 集合处理方法
print('# 集合处理方法')
D = {'p', 'y', 123}
D.add('t')
D.discard('y')
for item in D:
    print(item, end='')
print('  D:', D)

try:
    while True:
        print(D.pop(), end='')
except:
    pass
print('  D:', D)

# 集合类型应用场景
print('# 集合类型应用场景')
# 包含关系的比较
print('# 包含关系的比较', 'p' in A, {'p', 'y'} < A)
# 数据去重
print('# 数据去重')
ls = ['p', 'p', 'y', 'y', 123]
print(ls)
ls = list(set(ls))
print(ls)

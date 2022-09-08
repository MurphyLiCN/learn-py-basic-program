# 序列是具有先后关系的一组元素，参考数学的向量与含下标的序列，有字符串、元组、列表三种
ls = ['python',123,'io']
s = 'python123.io'
t = (1,2,3)
# 序号：正向递增（从0）与反向递减（从-1）
print('# 操作符: in, not in, + , * , 索引s[i] , 切片s[i:j:k]')
print(ls[::-1],s[::-1])
# 函数
print('# 函数')
print(len(s),min(s),max(s),s.index('o'),s.index('o',5),s.count('o'))
# 元组类型及操作（一旦创建不可修改)
print('# 元组类型及操作（一旦创建不可修改)')
print('创建：逗号分隔 or () or tuple()')
creature = 'cat','dog','tiger','human'
print(creature)
color = (0x001100,'blue',creature)
print(color)
print(color[-1][2])

# 列表类型与操作,元素可修改，使用[] or list() 创建
print('# 列表类型与操作,元素可修改，使用[] or list() 创建')

ls = ['cat','dog','tiger',1024]
print(ls)

ls[1:2] = [1,2,3,4]
print(ls)

del ls[::3]
print(ls)

lt = ls * 2
print(lt)
print(ls+lt)

ls.append(1234)
print(ls)
ls.insert(3,'human')
print(ls)
ls.reverse()
print(ls)

# 应用场景：有序数据的表示




# 数据组织的维度，存储《》表示《》操作
# %%
# 一维数据的表示，有序列表、无序集合
ls = ['中', '日', '韩']
st = {'中', '日', '韩'}
# %%
# 一维数据的存储：空格分隔不换行、逗号分隔、特殊符号分隔
# %%
# 一维数据的操作：存储《》表示
f = open('/Users/murphy/学业/python/学习-程序设计/数据文件/7.3空格分隔写入.txt', 'w')
f.write(' '.join(ls))
f.close()

txt = open('/Users/murphy/学业/python/学习-程序设计/数据文件/7.3空格分隔.txt').read()
read_ls = txt.split(' ')
f.close()
#%%

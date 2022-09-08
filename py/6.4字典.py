# 字典：可以自定义索引的映射组合，键值对之间无序，使用{} or dict() 创建，：表示键值对
print('# 字典：可以自定义索引的映射组合，键值对之间无序，使用{} or dict() 创建，：表示键值对')
d = {'中国': '北京', '美国': '华盛顿', '法国': '巴黎'}
d['日本'] = '东京'
print(d, d['中国'])
# 函数与方法
print('# 函数与方法')
print(d.keys(), d.values(), d.items())
print( '中国' in d, '北京' in d)
print(d.get('中国','haha'),d.get('俄罗斯','haha'))
print(d, d.popitem(),d)


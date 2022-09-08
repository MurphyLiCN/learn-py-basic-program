# 英文
def get_tex():
    txt = open('/Users/murphy/学业/python/学习-程序设计/数据文件/hamlet.txt', 'r').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~\n':
        txt = txt.replace(ch, ' ')
    return txt


hamlet_txt = get_tex()
words = hamlet_txt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print('{0:<10}{1:>5}'.format(word, count))



import requests

r = requests.get('https://python123.io/ws/demo.html')
demo = r.text
# %%
from bs4 import BeautifulSoup

soup = BeautifulSoup(demo, 'html.parser')
print(soup.prettify())
# %% 标签： <姓名 属性（字典）>...（字符串）</姓名>
# %% 获取标签
tag = soup.a
type(tag)
#%% 标签名
print(tag)
print(tag.name)
print(tag.parent.name)
print(tag.parent.parent.name)
#%% 标签属性
print(tag.attrs)
print(type(tag.attrs))
print(tag.attrs['class'])
print(tag.attrs['id'])
print(tag.attrs['href'])
#%% 内容字符串
print(tag.string)
print(soup.p)
print(soup.p.string)
print(type(soup.p.string))
#%% 注释
newsoup = BeautifulSoup('<b><!--这是注释--></b><p>这不是注释</p>','html.parser')
print(newsoup.b.string)
print(type(newsoup.b.string))
print(newsoup.p.string)
print(type(newsoup.p.string))
#%% 遍历：下行
print(soup.head)
print(soup.head.contents)
print(soup.body)
print(soup.body.contents[1])
print(len(soup.body.contents))
#%% 遍历：上行
print(soup.a.parent)
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
#%% 遍历：平行
print(soup.a.next_sibling)
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling)
#%% html的格式化与编码
print(soup.a.prettify())
#%% 信息标记形式：SML JSON YAML
#%% 信息提取：解析与搜索的融合使用
for link in soup.find_all('a'):
    print(link.get('href'))
#%%
for tag in soup.find_all(True):
    print(tag.name)
#%% 正则匹配
import re
for tag in soup.find_all(re.compile('b')):
    print(tag.name)
#%%
print(soup.find_all(id='link1'))
#%%
print(soup.find_all('a'))
print(soup.find_all('a',recursive=False))
#%%
print(soup.find_all(string = re.compile('python')))
#%%

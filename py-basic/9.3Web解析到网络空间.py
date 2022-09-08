# 网络爬虫：Rquests（页面级）、Scrapy（框架）、pyspider（系统）
import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code,
      r.headers['content-type'],
      r.encoding,
      r.text)
# %%
# Web信息提取：Beautiful Soup（HTML与XML解析）
# Regular Expression（Re 正则表达式解析）
# Python-Goose（提取文章、视频类型）
from goose import Goose
url = 'http://www.elmundo.es/elmundo/2012/10/28/espana/1351388909.html'
g = Goose({'use_meta_language': False, 'target_language': 'es'})
article = g.extract(url=url)
article.cleaned_text[:150]

# %%
# web开发 Django（复杂专业）Pyramid（规模适中）Flask（简单规模小）
from flask import Flask
app = Flask(_name_)
@app.route('/')
def hello_world():
    return 'Hello,World!'
#%%
# 网络应用开发：WeRoBot（微信公众号） aip（百度AI） MyQR（生成二维码）
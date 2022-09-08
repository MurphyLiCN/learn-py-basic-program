import requests

# 其实只有request一个方法，其他方法都是基于此的封装
# %% get()方法
r = requests.get('https://www.baidu.com')
print(r.status_code, '200代表正常')
print(type(r), r.headers)
# %% 乱码
r.text
# %% 'ISO-8859-1'代表header中无chartest
r.encoding
# %% 从内容中分析编码
r.apparent_encoding
# %% 替换编码方法
r.encoding = 'utf-8'
r.text
# %% 通用代码框架
import requests


def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 状态码不是200则产生异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'


if __name__ == '__main__':
    url = 'https://www.baidu.com'
    print(get_html_text(url))
    url = 'www.baidu.com'
    print(get_html_text(url))
# %% HTTP协议与方法：
# url：http://host[:post][path]
# 方法：get、head、post、put、patch、delete

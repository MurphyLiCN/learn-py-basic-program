import requests
kv = {'user-agent':'Mozilla/5.0'}
url = 'https://www.amazon.cn/dp/B00AA7KJQ8/ref=sr_1_3?__mk_zh_CN=亚马逊网站&crid=S3BXW6EAN8GW&keywords=书&qid=1658796864&sprefix=su%2Caps%2C83&sr=8-3'
try:
    r =requests.get(url,headers=kv)
    r.raise_for_status()
    print(r.text[1000:2000])
except:
    print('失败')
#%%
r.request.headers


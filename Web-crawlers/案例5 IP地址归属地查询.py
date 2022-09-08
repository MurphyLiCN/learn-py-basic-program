import requests
ip = '111.16.132.196'
url = 'https://www.ipshudi.com/'+ip+'/'
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-2300:-2100])
except:
    print('查询失败')

#%%

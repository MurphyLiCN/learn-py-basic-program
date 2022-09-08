import requests
url = 'https://item.jd.com/100026809200.html'
try:
    r =requests.get(url)
    r.raise_for_status()
    print(r.text[:1000])
except:
    print('失败')

#%%

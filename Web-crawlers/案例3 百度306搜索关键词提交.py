import requests

kv = {'q': 'python'}
url = 'https://www.so.com/s'
r = requests.get(url, params=kv)
r.status_code
# %%
r.request.url
# %%
len(r.text)
#%%

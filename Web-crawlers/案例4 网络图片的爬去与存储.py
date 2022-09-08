import requests
import os
root = '/Users/murphy/学业/python/学习-爬虫/文件/'
url = 'https://www.worldphoto.org/sites/default/files/2%20Amelie%2C%20Labourdette%2C%20France%2C%201st%20Place%2C%20Profressional%2C%20Architecture%2C%202016%20Sony%20World%20Photography%20Awards.jpg'
path = root + url.split('/')[-1][-10:]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')

#%%

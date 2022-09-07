import wordcloud
import jieba
from imageio import imread

# 设计形状
mask = imread('/Users/murphy/学业/python/学习-程序设计/数据文件/五角星.png')
# 读入处理处理文本
f = open('/Users/murphy/学业/python/学习-程序设计/数据文件/新时代中国特色社会主义.txt'
         , 'r', encoding='utf-8')
t = f.read()
f.close()

ls = jieba.lcut(t)
new_ls = [item for item in ls if len(item)>1]

txt = ' '.join(new_ls)
# 配置对象参数
c = wordcloud.WordCloud(width=1000, height=700,
                        background_color='white',
                        font_path="/System/Library/fonts/PingFang.ttc",
                        max_words=40,
                        mask = mask)
# 加载词云文本
c.generate(txt)
# 内部处理：1.空格分隔 2.统计过滤 3.配置字体 4.布局
# 输出词云文件
c.to_file('/Users/murphy/学业/python/学习-程序设计/数据文件/wc_新时代中国特色社会主义.png')

#%%

import wordcloud
import jieba
# 处理文本
txt = '复旦复旦旦复旦，巍巍学府文章焕，' \
      '学术独立思想自由，政罗教网无羁绊，' \
      '无羁绊前程远，向前，向前，向前进展。' \
      '复旦复旦旦复旦，日月光华同灿烂。'
wc_txt = ' '.join(jieba.lcut(txt))
# 配置对象参数
c = wordcloud.WordCloud(width=1000,height=700,
                        background_color='black',
                        font_path="/System/Library/fonts/PingFang.ttc")
# 加载词云文本
c.generate(wc_txt)
# 内部处理：1.空格分隔 2.统计过滤 3.配置字体 4.布局
# 输出词云文件
c.to_file('/Users/murphy/学业/python/学习-程序设计/数据文件/pywordcloud.png')
#%%

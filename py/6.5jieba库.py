import jieba
print(jieba.lcut('中华人民共和国是一个伟大的国家'))
print(jieba.lcut('中华人民共和国是一个伟大的国家',cut_all = True))
print(jieba.lcut_for_search('中华人民共和国是一个伟大的国家'))
print(jieba.lcut('中华人民共和国是一个伟大的国家',use_paddle = True))

#输入数字输出汉字
weelkstr = '一二三四五六日'
weekid = eval(input('请输入星期数字(1-7):'))
pos = weelkstr[weekid-1]
print('星期'+pos)
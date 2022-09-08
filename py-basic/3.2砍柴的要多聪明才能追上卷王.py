# 如题
def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [0, 6]:
            dayup *= 1 - 0.01
        else:
            dayup *= 1 + df
    return dayup


df = 0.01
while dayUP(df) < 37.78:
    df += 0.001
print('需要{:.5f}'.format(df))

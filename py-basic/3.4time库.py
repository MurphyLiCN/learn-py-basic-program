import time
#获取时间
print('#获取时间')
print(time.time(),'\n',
      time.ctime(),'\n',
      time.gmtime(),'\n',
      )
#格式化时间
print('#格式化时间')
print(time.strftime('%Y-%m-%d %H:%M:%S %I%p %B-%b-%A-%a',time.gmtime()),'\n',
      time.strptime('2022-07-12 12:38:14','%Y-%m-%d %H:%M:%S'))
#程序计时
print('#程序计时')
start=time.perf_counter()
time.sleep(3.3)
end=time.perf_counter()
all_time=end-start



index = input("输入一个整数")
index = eval(index)
if index == 0:
    print('Hello World')
elif index > 0:
    string = 'Hello World'
    s = "";
    for n in range(len(string)):
        if (n + 1) % 2 != 0:
            s = s + string[n];
            if len(string) == (n + 1):
                print(s);
        else:
            s = s + string[n];
            print(s);
            s = "";
else:
    for i in 'Hello World':
        print(i)

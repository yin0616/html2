#99乘法表
for i in range(1,10):
    for j in range(1,10):
        print("%d * %d = %02d" % (i,j,j*i), end = ("  "))
    print()

#梯形
for i in range(1,8):
    print("*" * i)

#三角形
for i in range(1,8):
    print(' ' *(7-i)+'*'*(2*i-1))

#菱形
for i in range(1,8):
    print(' ' * (7-i) + "*"*(2*i-1))
for i in reversed(range(1,7)):
    print(' ' * (7-i) + "*"*(2*i-1))


 
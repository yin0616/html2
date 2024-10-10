import random
num = random.randint(1, 100)
print("從1到100猜一個數字")
while True:
    a = int(input())
    if (a == num):
        print("對了")
        break
    else:
        print("繼續猜")

def no():
    if(a>num):
        print("範圍在",a,"和")




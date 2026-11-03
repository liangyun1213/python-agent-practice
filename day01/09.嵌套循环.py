#嵌套循环
#根据输入的长方形长度m，宽度n，打印一个长方形；
m = int(input("请输入长方形的长："))
n = int(input("请输入长方形的宽："))
for i in range(n):
    for j in range(m):
        print("*",end="\t")
    print()

#打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()

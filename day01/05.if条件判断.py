#if条件判断
#完成B站登录功能的实现（正确账号和密码为18888888888/666888）
ok_account = 18888888888
ok_password = 666888
account = int(input("请输入你的账号："))
password = int(input("请输入你的密码"))
if account == ok_account and password == ok_password:
    print("账号密码正确，登录成功")
else:
    print("账号或密码错误！")

#根据用户输入的年份判断这一年是闰年还是平年
year = int(input("请输入年份："))
if year % 100 == 0 and year % 400 == 0:
    print("是闰年")
elif year % 100 != 0 and year % 4 == 0:
    print("是闰年")
else:
    print("是平年")
#根据输入的三个边的边长（正整数），判定是等边三角形、等腰三角形、普通三角形，还是不能构成三角型
print("请输入三个边的边长")
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    if a == b and a == c:
        print("这个三角形是等边三角形")
    elif a == b or b == c or a == c:
        print("这个三角形是等腰三角形")
    else:
        print("这个三角形是普通三角形")
else:
    print("这三条边不能构成三角形")

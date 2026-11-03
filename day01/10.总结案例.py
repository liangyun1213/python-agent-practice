"""
根据输入的用户名密码执行登录操作，具体要求如下：
1.正确的用户名和密码为admin/666888、zhangsan/123456、taoge/888666
2.输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
3.输入用户名和密码不能为空！
4.登陆成功：输出“登录成功，进入B站首页~”
5.登录失败:输出“用户名或密码错误，请重新输入！”
"""
# from random import random
#
# while True:
#     user = input("请输入用户名")
#     password = input("请输入密码")
#     if user == "" or password == "":
#         print("输入的用户名和密码不能为空！请重新输入！")
#         continue #结束当前循环，直接进入下一轮循环
#     if (user == "admin" and password == "666888") or(user == "zhangsan" and password == "123456") or (user == "taoge" and password == "888666"):
#         print("登录成功，进入B站首页~")
#         break#只能出现在循环中，表示结束，跳出循环
#     else:
#         print("用户名或密码错误，请重新输入！")



#猜数字游戏
"""
1.系统随机生成一个随机数
2.用户根据提示猜数字，并将所采的数字输入系统
3.如果猜错，系统给出提示是猜大了，还是猜小了，然后继续猜数字
4.如果猜对，系统自动退出，游戏结束
"""
import random
random_num = random.randint(1,100)
while True:
    num = int(input("请输入你要猜的数字："))
    if num > random_num:
        print("猜大了")
    elif num < random_num:
        print("猜小了")
    else:
        print("你猜对啦！")
        break

print("随机生成的数字是：",random_num)
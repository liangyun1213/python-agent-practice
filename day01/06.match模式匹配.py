#match...case 模式匹配 ：工作日程安排
# day = input("请输入星期几（1-7）：")
# match day:
#     case "1":
#         print("周一：工作会议日")
#     case "2":
#         print("周二：学习培训日")
#     case "3":
#         print("周三：项目开发日")
#     case "4":
#         print("周四：代码审查日")
#     case "5":
#         print("周五：总结规划日")
#     case "6"|"7":
#         print("周末：休息放松")
#     case _:
#         print("输入有误！")


#实现一个计算器，可以实现+-*/运算，用户输入需要运算的两个数以及运算符之后，就可以进行计算。
print("请输入运算的两个数：")
a = float(input())
b = float(input())
print("请输入运算符：")
c = input()
match c:
    case "+":
        print(f"{a} + {b} = {a + b}")
    case "-":
        print(f"{a} - {b} = {a - b}")
    case "*":
        print(f"{a} * {b} = {a * b}")
    case "/" if b != 0:
        print(f"{a} / {b} = {a / b}")
    case _:
        print("输入错误！")


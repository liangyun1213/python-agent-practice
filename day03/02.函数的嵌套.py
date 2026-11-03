#函数的嵌套：在一个函数中又调用了另一个函数
#函数调用遵循栈结构，后进先出（弹夹使用）
def function_a():
    print("a...before")
    function_b()
    print("a...after")

def function_b():
    print("b...before")
    function_c()
    print("b...after")

def function_c():
    print("c...")
print(function_a())

#1.定义一个函数：根据传入的底盒高计算三角形面积的函数
def triangle_area(d,h):
    """
    该函数用于根据三角形的底和高，计算三角形的面积
    :param d: 三角形的底
    :param h: 三角形的高
    :return: 三角形的面积
    """
    area = d * h / 2
    return area
d = float(input("请输入三角形的底："))
h = float(input("请输入三角形的高："))
print("三角形的面积为：",triangle_area(d,h))

#2.定义一个函数，计算传入的字符串中元音字母的个数（元音字母为aeiouAEIOU）
def count_aeiou(s):
    num = 0
    for w in s:
        if w in "aeiouAEIOU":
            num += 1
    return num
s = input("请输入字符串：")
total = count_aeiou(s)
print("其中元音字母的个数是：",total)


#3.定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1为小数），并返回。
def statistics_score(socre_list):
    """
    该函数根据班级学员的高考成绩，计算其中最高分、最低分、平均分
    :param dict: 班级学员的高考成绩
    :return: 最高分、最低分、平均分
    """
    max_score = max(socre_list)
    min_score = min(socre_list)
    total = sum(socre_list)
    age = round((total / len(socre_list)),1)
    return max_score,min_score,age

s_list = [589,609,605,643,677,455,477,489,503]
print("该列表中的最高分、最低分、平均分分别是：",statistics_score(s_list))


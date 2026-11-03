"""
开发一个教务管理系统，在该系统中可以维护和管理学院的成绩信息，具体需求如下：
1.添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
2.修改学生信息：要求输入要修改的学生姓名，然后载体是输入语文、数学、英语成绩，输入完成后修改学员信息。
3.删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
4.查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
5.列出所有学生：遍历所有学生信息并输出。
6.退出系统。
"""
students = {}
while True:
    print("""
    # # # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # #
    # 1.添加学生信息    2.修改学生信息    3.删除学生信息    4.查询学生信息    5.列出所有学生    6.统计班级成绩    7.退出系统     #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    \n
    """)
    choice = input("请选择要执行的操作（1-7）：")
    match choice:
        case "1":# 添加学生信息
            name = input("请输入学生姓名：")
            if name in students:
                print("该学生已存在系统内部！")
            else:
                chinese_grades = float(input("请输入语文成绩："))
                math_grades = float(input("请输入数学成绩："))
                english_grades = float(input("请输入英语成绩："))
                students[name] = {name: {"语文": chinese_grades, "数学": math_grades, "英语": english_grades}}
                print("添加成功")
        case "2":# 修改学生信息
            name = input("请输入要修改的学生姓名：")
            if name not in students:
                print("系统内没有该学生信息！")
            else:
                chinese_grades = float(input("请输入最新语文成绩："))
                math_grades = float(input("请输入最新数学成绩："))
                english_grades = float(input("请输入最新英语成绩："))
                students[name] = {name: {"语文": chinese_grades, "数学": math_grades, "英语": english_grades}}
                print("修改成功")
        case "3":# 删除学生信息
            name = input("请输入要删除的学生姓名：")
            if name not in students:
                print("系统内没有该学生信息！")
            else:
                del students[name]
                print("删除成功")
        case "4":# 查询学生信息
            name = input("请输入要查询的学生姓名")
            if name not in students:
                print("系统内没有该学生信息！")
            else:
                print(students[name])
        case "5":# 列出所有学生
            for s in students[name]:
                print(students[name])
        case "6":
            break
        case _:
            print("操作错误！！！")
    print("""
    \n
    # # # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # #
    # 1.添加学生信息    2.修改学生信息    3.删除学生信息    4.查询学生信息    5.列出所有学生    6.统计班级成绩    7.退出系统     #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    """)



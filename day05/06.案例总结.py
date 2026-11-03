"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
1.添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
2.修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
3.删除学生车成绩：根据输入的学生姓名，删除对应的学生成绩
4.查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
5.展示全部学生成绩
"""

class Student:
    def __init__(self,s_name = None,s_chinese = None,s_math = None,s_english = None):
        self.name = s_name
        self.chinese = s_chinese
        self.math = s_math
        self.english = s_english
    def __str__(self):
        return f"{self.name} {self.chinese} {self.math} {self.english}"

class EduManagement:
    systemo_version = "1.0"
    system_anme = "教务处管理系统"
    def __init__(self):
        self.student_list = []
    #添加学生信息
    def add_student(self):
        name = input("请输入学生姓名：")
        for student in self.student_list:
            if student.name == name:
                print("该学生已存在系统中！")
                return
        chinese = float(input("请输入语文成绩："))
        math = float(input("请输入数学成绩："))
        english = float(input("请输入英语成绩："))
        if chinese in range(0,101) and math in range(0,101) and english in range(0,101):
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("添加成功")
            return
        else:
            print("成绩超出范围！！！")
            return
    #修改学生信息
    def edit_student(self):
        name = input("请输入要修改成绩的学生姓名：")
        for student in self.student_list:
            if student.name == name:
                print(f"姓名：{student.name} | 语文：{student.chinese} | 数学：{student.math} | 英语：{student.english}")
                student.chinese = float(input("请输入新的语文成绩"))
                student.math = float(input("请输入新的语文成绩"))
                student.english = float(input("请输入新的英语成绩"))
                print("修改成功")
                print(f"姓名：{student.name} | 语文：{student.chinese} | 数学：{student.math} | 英语：{student.english}")
                return
            else:
                print("系统中不存在该学生信息！")
                return


    #删除学生信息
    def delete_student(self):
        name = input("请输入要删除成绩的学生姓名：")
        for student in self.student_list:
            if student.name == name:
                student.name = None
                student.chinese = None
                student.math = None
                student.english = None
                print("删除成功")
                return
            else:
                print("系统中不存在该学生信息！")
                return


    #查询指定学生信息
    def check_student(self):
        name = input("请输入要查询成绩的学生姓名：")
        for student in self.student_list:
            if student.name == name:
                total = student.chinese + student.math + student.english
                print(
                    f"姓名：{student.name} | 语文：{student.chinese} | 数学：{student.math} | 英语：{student.english} | 总分：{total}")
                return
            else:
                print("系统中不存在该学生信息！")


    #展示全部学生信息
    def total_student(self):
        for student in self.student_list:
            print(f"姓名：{student.name} | 语文：{student.chinese} | 数学：{student.math} | 英语：{student.english}")
    #运行系统
    def run(self):
        print("欢迎进入教务管理系统")
        print(
            "1.添加学生成绩\n2.修改学生成绩\n3.删除学生成绩\n4.查询指定学生成绩\n5.展示全部学生成绩\n6.退出教务管理系统")
        while True:
            choice = input("请输入操作程序：")
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.edit_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.check_student()
                case "5":
                    self.total_student()
                case "6":
                    break
                case _:
                    print("操作错误！！！")



if __name__ == "__main__":
    em = EduManagement()
    em.run()



#常见数据类型
#type()语句来得到数据的类型，语法：type(要查看类型的数据)
print(type("Hello word"))
print(type(10))
print(type(3.14))
print(type(True))
print(type(False))
print(type(None))
#通过isinstance()检查数据是否属于指定的类型，返回的是一个bool值，具体语法为isinstance(数据，类型)
num = 100
print(type(num))
print(isinstance(num,int))
print(isinstance(num,float))
print(isinstance(num,bool))
print(isinstance(num,str))


#字符串三种定义方式
s1 = "hello"#双引号
s2 = 'python'#单引号
s3 = """
Hello；
    欢迎进入Python世界
    """#三引号(多行字符串)
print(s1)
print(s2)
print(s3)

#根据自己的实际情况，输出个人的相信信息，具体结果如下：“大家好，我是涛哥，今年18岁，学习的专业是软件工程，爱好Python、java”
name = input("请输入你的姓名")
age = input("请输入你的年龄")
major = input("请输入你的专业")
hobby = input("请输入你的爱好")
print(f"大家好，我是{name},今年{age}岁，学习的专业是{major}，爱好是{hobby}")
print("大家好，我是%s,今年%s岁，学习的专业是%s，爱好是%s"%(name,age,major,hobby))

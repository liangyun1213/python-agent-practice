#定义类---->不推荐动态的为对象添加属性
#类名的命名规范，遵循大驼峰命名法，每个单词的首字母都是大写，单词之间没有分隔符，比如UserInfo,UserAccount.
class Car:
    pass
#创建对象
# 对象名 = 类名()
# 对象名.属性名1 = 属性值1
# 对象名.属性名2 = 属性值2
c1 = Car()
c1.brand = "BMW"
c1.name = "X5"
c1.price = 500000
print(c1.brand)
#__dict__时Python中用户自定义类势力的一个特殊属性，用于以字典形式存储对象的属性。
print(c1.__dict__)

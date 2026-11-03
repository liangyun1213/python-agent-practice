#魔法方法：Python中提供以双下划线开头和结尾的特殊方法，用于定义类的特殊行为，比如__init__.
#不需要手动调用，Python会在合适的时机自动调用
#__init__                     初始化方法
#__str__                      字符串表示的方法
#__eq__                       比较两个对象是否相等（equal）
#__lt__（小于）,__le__（小于等于）,__gt__（大于）,__ge__（大于等于）  支持比较两个对象的大小
class Car:
    def __init__(self,c_brand,c_name,c_price):
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
    def running(self):
        print(f"{self.brand} {self.name}正在高速行驶")
    def __str__(self):
        return f"{self.brand} {self.name} {self.price}"
    def __eq__(self, other):
        return self.brand == other.brand and self.name == other.name and self.price == other.price
    def __lt__(self, other):
        return self.price < other.price

c1 = Car("BMW","X5",500000)
print(c1)
c2 = Car("BMW","X5",500000)
print(c2)
print(c1 == c2)
print(c1 < c2)
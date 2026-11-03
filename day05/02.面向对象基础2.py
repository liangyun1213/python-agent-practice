#定义类
class Car:
    #__init__ 方法是初始化的方法，会在对象创建时自动调用，可以再该方法中为对象设置对应的属性。
    #self：是第一个参数，表示当前所创建出来的实例对象
    def __init__(self,c_brand,c_name,c_price):
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car类型的对象初始化完毕，对象属性已经添加完毕。")
#创建对象
c1 = Car("BMW","X5",500000)
print(c1.__dict__)
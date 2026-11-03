#实例属性：属于每个对象的属性，每个对象都是独立的。（各个对象特有的数据）
#类属性：类属性是属于类本身的属性，所有实例共享的（所有对象共享的数据或配置）
#类属性（通过类名.属性的方式操作）
#实例属性（通过实例对象.属性的方式操作）
class Car:
    wheel = 4 #轮胎数量，类属性
    tax_rate = 0.1 #购置税，类属性
    def __init__(self,c_brand,c_name,c_price):
        self.brand = c_brand #实例属性
        self.name = c_name #实例属性
        self.price = c_price #实例属性
    def running(self):
        print(f"{self.brand} {self.name}正在高速行驶")

#实例属性查找属性时，会先查找实例属性，实例属性不存在时，再查找类属性
c1 = Car("BMW","X5",500000)
c2 = Car("奔驰","e300",1800000)
print(c1.brand)
print(c1.wheel)
print(Car.wheel)
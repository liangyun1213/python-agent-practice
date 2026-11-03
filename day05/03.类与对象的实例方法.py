class Car:
    def __init__(self,c_brand,c_name,c_price):
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
    #定义类实例方法
    def running(self):
        print(f"{self.brand} {self.name}正在高速行驶")
    def total_cost(self,discount,rate):
        return self.price * discount + self.price * rate

#测试
c1 = Car("BMW","X5",500000)
total_cost = c1.total_cost(0.9,0.1)
print(f"提车总价为：{total_cost:.0f}")
c1.running()
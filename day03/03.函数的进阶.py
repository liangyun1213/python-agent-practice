#函数的进阶
#global:在函数中要使用全局变量，使得可以在函数内部修改全局变量的值
num1 = 1  #全局变量
def fun1():
    num1 = 100  #局部变量
    print(num1)
fun1() #100
print(num1) #1
def fun2():
    global num1
    num1 = 100 #修改全局变量num1
    print(num1)
fun2() #100
print(num1) #100


#不定长参数也叫可变参数，用户函数定义及调用是参数个数不确定（0个或多个）的场景
#类型：位置传递（*args），关键字传递（**kwargs）
#args是元组类型，args只是约定俗成的变量名，也可以使用任何合法的变量名（*data）
#args适用于处理数量不确定的数据
#根据传入的这批数据，计算这批数据的最小值，最大值，平均值
def calc_data1(*args):
 min_data = min(args)
 max_data = max(args)
 avg_data = sum(args) / len(args)
 return min_data,max_data,round(avg_data,1)
data = calc_data1(1,2,3,4,5,6,7,8,9)
print(data)

data = calc_data1(10,20,30,40,50)
print(data)

#kwargs是字典类型，kwargs只是约定俗成的变量名，也可以使用任何合法的变量名（**data）
#**kwargs适用于处理数量不确定的选项
def calc_data2(*args,**kwargs):
 min_data = min(args)
 max_data = max(args)
 avg_data = sum(args) / len(args)
 if kwargs.get("round") is not None:
     avg_data = round(avg_data,kwargs.get("round"))
 if kwargs.get("print"):
     print(f"计算出来的最小值：{min_data},最大值：{max_data}，平均值：{avg_data}")
 return min_data,max_data,avg_data
print(calc_data2(2,7,9,10,45,round = 3,print = True))


#函数的参数类型：各种数据类型、数据容器、函数。
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def calc(x,y,oper):
    return oper(x,y)
result = calc(10,20,add)
print(result)

#匿名函数：没有名称的函数，需要通过lambda表达式来声明函数，可以简化简单函数的编写（单行表达式）。
# lambda 参数列表： 函数体
out_line = lambda:print("-------------")
add = lambda x,y:x+y
out_line()
print(add(1,2))
#按照每一个元素的字符个数，从小到大排序
data_list = ["C++","C","Python","Jack","PHP","Java","Go","JavaScript","Rust"]
data_list.sort(key=lambda item:len(item))#匿名函数典型的应用场景
print(data_list)


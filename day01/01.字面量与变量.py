#字面量的写法
print(100)#整数（int）
print(3.14)#浮点数（float）
print(True)#布尔（bool）
print(False)#布尔（bool）
print("Hello word")#字符串（str）
print("-------------")#字符串（str）
print(None)#空值（NoneType）

#变量---->Python是动态类型语言，可以存储不同类型的数据
num = 1114.1
print(num)
num = num + 1
print(num)
num = "ok"
print(num)

a = 20.7
b = 50
first_m = a + b
second_m = first_m + b
print("未来第一个月的播放量是",first_m)
print("未来第二个月的播放量是",second_m)

#现在有两个变量，分别为a = 100，b = 200，c = 300,现在需要将这三个变量值交换，将a，b，c的值分别赋值给c，啊，
# b，然后输出到控制台
a = 100
b = 200
c = 300
temp = a
a = b
b = c
c = temp
print(a,b,c)

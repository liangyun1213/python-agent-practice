#字典的了解 存储键值对（key；value）类型的数据，可以根据键（key）找到相对应的值（value）。
#定义字典存储
dict1 = {"王林":670,"韩立":556,"李慕婉":582,"紫灵":435,"徐立国":608}
#键值对存储，键不能修重复、可修改(int,float,tuble,str)
#定义空字典
dict2 = {}
dict3 = dict()
print(dict1["王林"])

#添加：dict[key] = value 往指定字典中添加key-value键值对
#删除：score = dict.pop("key") 删除字典中指定的key，并返回该key对应的value
#删除：del dict["key"] 删除字典中指定的键值对
#修改：dict[key] = value 修改字典中指定的key对应的值
#查询：dict["key"] 根据key获取value
#查询：dict.get(key) 根据key获取value
#查询：dict.keys() 获取所有的key
#查询：dict.value() 获取所有的value
#查询：dict.items() 获取所有的键值对key-value

#遍历
for k in dict1.keys():
    print(f"{k}:{dict1[k]}")

for item in dict1.items():
    print(f"{item[0]}:{item[1]}")
for k,v in dict1.items():
    print(f"{k}:{v}")

"""
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
1.添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车
2.修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改改商评信息。
3.删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
4.查询购物车：将购物车中的商品信息展示出来，格式为：“商品名称：xxx，商品价格：xxx，商品数量”。
5.退出购物车
"""
shopping_cart = {}
# while True:
#     name = input("请输入商品名称：")
#     price = int(input("请输入商品价格："))
#     num = int(input("请输入商品数量："))
#     shopping_cart[name] = {name:{"商品价格":price,"商品数量":num}}
#     print("是否退出，是请输出-1，否则按任意键")
#     Return = input()
#     if Return == -1:
#         break
# name = input("请输入要修改的商品名称：")
# price = int(input("请输入要修改的商品价格："))
# num = int(input("请输入要修改的商品数量："))
# shopping_cart[name] = {name:{"商品价格":price,"商品数量":num}}
#
# name = input("请输入要删除的商品名称：")
# del shopping_cart[name]
#
# name = input("请输入要查询的商品名称：")
# print(shopping_cart[name])

print("欢迎使用购物车管理系统！")
print()
print("""
########## 购物车系统 ##########
#        1.添加购物车          #
#        2.修改购物车          #
#        3.删除购物车          #
#        4.查询购物车          #
#        5.退出购物车          #
##############################：
""")
while True:
    a = input("请选择要执行的操作（1-5）：")
    match a:
        case "1":
            name = input("请输入商品名称：")
            price = int(input("请输入商品价格："))
            num = int(input("请输入商品数量："))
            shopping_cart[name] = {name: {"商品价格": price, "商品数量": num}}
        case "2":
            name = input("请输入要修改的商品名称：")
            price = int(input("请输入要修改的商品价格："))
            num = int(input("请输入要修改的商品数量："))
            shopping_cart[name] = {name: {"商品价格": price, "商品数量": num}}
        case "3":
            name = input("请输入要删除的商品名称：")
            del shopping_cart[name]
        case "4":
            name = input("请输入要查询的商品名称：")
            print(shopping_cart[name])
        case "5":
            break
        case _:
            print("输入错误请重新输入")
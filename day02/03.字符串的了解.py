#切片索引
#s.find("Python") 在字符串中查找子串，返回第一次出现的索引位置，找不到返回-1
#s.count("H") 统计子串在字符串中出现的次数
#s.upper() 将字符串中的所有字母转换为大写
#s.lower() 将字符串中的所有字母转换为小写
#s.split(' ') 将字符串按指定分隔符分割成列表
#s.strip('*') 去除字符串两端的空白字符或指定字符
#s.replace("H" "C") 将字符串中的指定子串替换原来的子串
#s.startswith("P") 检查字符串是否以指定子串开头，返回布尔值
#s.endswith("P") 检查字符串是否以指定子串结尾，返回布尔值
s = "Hello-Python-Hello-World"
# print(s)
# print(s[0:5:2])
#
# for i in s:
#     print(i)
# print(s.find("h"))
# print(s.count("o"))
# print(s.upper())
# print(s.lower())
# print(s.split("-"))
# print(s.strip("-"))
# print(s.replace("World","Java"))
# print(s.startswith("A"))
# print(s.endswith("World"))


#用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.），如果输入正确，输出邮箱格式正确，否则输出“邮箱格式错误”。
email = input("请输入邮箱：")
#方式1
if email.count("@") == 1 and email.count(".") >= 1:
    print("邮箱格式正确")
else :
    print("邮箱格式错误")
#方式2：in 运算符---->判断子串是否存在于字符串中，存在返回True，否则返回False
if email.count("@") == 1 and "."in email:
    print("邮箱格式正确")
else :
    print("邮箱格式错误")
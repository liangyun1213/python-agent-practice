import json

#写入json文件
# user = {
#     "name" : "凉韵",
#     "age" : 18,
#     "gender" : "男",
#     "hobbies" : ["篮球","游戏"]
# }
# with open("resources/user.json","w",encoding="utf-8") as f:
#     #ensure_ascii=False,indent=4,表示不使用ascii编码，且缩进为4
#     json.dump(user,f,ensure_ascii=False,indent=4)

#读取json数据文件
with open("resources/user.json","r",encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))

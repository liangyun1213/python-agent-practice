#集合的了解：无序的、不可重复的、可修改的
s1 = {"A","B","C","D"}
s2 = set()
# s1.add("t") 添加元素到集合中
# s1.remove("t") 移除集合中的指定元素（指定元素不存在将报错）
# s1.pop() 随机删除集合中的元素并返回
# s1.clear() 清空集合
# s1.difference(s2) 求取两个集合的差集（包含在第一个集合但不包含在第二个集合的元素）
# s1.union(s2) 求取两个集合的并集
# s1.intersection(s2) 求取两个集合的交集

"""
根据提供的班级学生的选课情况，完成如下需求：
1.找出同时选修了法语和艺术的学生
2.找出同时选修了所有四门课程的学生
3.找出选修了足球，但是没有选修篮球的学生
4.统计每一个学生选修的课程数量
"""
football_set = {"王林","曾牛","徐立国","遁天","天运子","韩立","历飞雨","乌丑","紫灵"}
basketball_set = {"张铁","墨居仁","王林","姜老道","曾牛","王婵","韩立","天运子","李化元","历飞雨","云露"}
french_set = {"许木","王卓","十三","虎咆","姜老道","天运子","红蝶","历飞雨","韩立","曾牛"}
art_set = {"遁天","天运子","韩立","虎咆","姜老道","紫灵"}
print("同时选修了法语和艺术的学生：",french_set.intersection(art_set))
print("找出同时选修了所有四门课程的学生:",football_set.intersection(basketball_set.intersection(football_set.intersection(art_set))))
print("修了足球，但是没有选修篮球的学生:",football_set.difference(basketball_set))
#student_set = football_set.union(basketball_set.union(football_set.union(art_set)))
student_set = football_set|basketball_set|french_set|art_set
print(student_set)
all_list = [*football_set,*basketball_set,*french_set,*art_set]
for s in student_set:
    print(f"{s}选修了{all_list.count(s)}课程")

#元组的了解：重复，有序，不可修改
t1 = (1,2,3,4,5,6,42,65,75)
t2 = ()
t3 = tuple()
#t.count():统计某元素在元组中出现的次数
#t.index():查找某个元素在元组中的索引位置（第一次出现的位置）
print(t1)
print(type(t1))

#索引访问
print(t1[0])

#切片
print(t1[0:5:2])

print(t1.count(87))

print(t1.index(4))


#组包：将多个值合并到一个容器中
t1 = (1,2,3,4)
#解包：将容器解开成独立的元素，分别赋值给多个变量
a,b,c,d = t1
print(a,b,c,d)
#(*)扩展解包:*收集剩余所有元素
t2 = (5,7,9,1)
x,*y,z = t2
print(x,y,z)
s,*o = t2
print(s,o)
*o,e = t2
print(o,e)
a,b = 10,20
a,b = b,a
print(a,b)

"""
根据提供的学生成绩单，完成如下需求：
1.计算每个学生的总分、各科平均分，然后一并输出出来.
2.统计各科成绩的最低分、最高分、平均分，并输出。
3.查找成绩优秀（平均分大于90）的学生，并输出
"""
students = (
    ("s001","王林",85,92,78),
    ("s002","李慕婉",92,88,95),
    ("s003","十三",78,85,82),
    ("s004","曾牛",88,79,91),
    ("s005","周轶",95,96,89),
    ("s006","王卓",76,82,77),
    ("s007","红蝶",89,91,94),
    ("s008","徐立国",75,69,82),
    ("s009","许木",86,89,98),
    ("s010","遁天",66,59,72)
)
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for student in students:
    total = student[2] + student[3] + student[4]
    avg = total / 3
    print(f"{student[0]} \t {student[1]} \t {student[2]} \t {student[3]} \t {student[4]} \t {total} \t {avg:.1f}")
chinese_scores = [student[2] for student in students]
print(f"语文最低分：{min(chinese_scores)},语文最高分：{max(chinese_scores)},平均分：{sum(chinese_scores)/len(chinese_scores)}")
math_scores = [student[3] for student in students]
print(f"数学最低分：{min(math_scores)},数学最高分：{max(math_scores)},平均分：{sum(math_scores)/len(math_scores)}")
english_scores = [student[4] for student in students]
print(f"英语最低分：{min(english_scores)},英语最高分：{max(english_scores)},平均分：{sum(english_scores)/len(english_scores)}")
for student in students:
    total = student[2] + student[3] + student[4]
    avg = total / 3
    if avg >= 90:
        print(f"成绩优秀的学生为：{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{total}\t{avg:.1f}")
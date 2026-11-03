# s.append(234) 列表尾部追加元素
# s.insert(0，34) 再指定索引前插入该元素
# s.remove(56) 移除列表中第一个匹配到的值
# s.pop(3) 删除列表中指定索引位置的元素（未指定则删除最后一个）
# s.sort()对列表进行排序（元素数据类型一致）
# s.reverse()反转列表元素


#将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和平均值
# print("请输入10个数字")
# s = []
# for i in range(10):
#     s.append(int(input()))
# print(s)
# s.sort()
# print(s)
# print("列表中的最小值：",s[0],"列表中的最大值：",s[-1],"列表的平均值",sum(s) / len(s))
# #sum()求和，len()获取元素的个数


# #合并两个列表中的元素，并对合并的结果进行去重处理
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# #循环遍历
# # for num in num_list2:
# #     num_list1.append(num)
# #解包：将列表这一类容易拆解成一个一个独立元素
# #组包：将多个值合并到一个容器
# num_list = [*num_list1,*num_list2]
# print("合并后的列表：",num_list1)
#
# new_list = []
# for num in num_list1:
#     if num not in new_list:
#         new_list.append(num)
# print("去重后的列表：",new_list)

#1.生成1-20的平方列表
square_list = []
for i in range(1,21):
    square_list.append(i**2)
print("1-20的平方列表：",square_list)
#2.从如下数字列表表中提取所欲偶数，并计算其平方，组成一个新的列表。
num_list = [19,23,54,64,87,20,109,232,123,43,26,55,72]
new_list = []
for num in num_list:
    if num % 2 == 0:
        new_list.append(num**2)
print("新的列表为：",new_list)
#读文件

#1.打开文件
# f = open("resources/望庐山瀑布.txt","r",encoding="utf-8")
#2.读取文件内容
#全部读取
# content = f.read()
# print(content)
#按行读取
# content1 = f.readlines()
# for line in content1:
#     print(line.strip())
#按行中字读取
# content2 = f.readline()
# for line in content2:
#     print(line)
# #3.关闭文件
# f.close()

#==================方式一================================
# #写文件
# #1.打开文件
# f = open("resources/静夜思.txt","w",encoding="utf-8")
# try:
#     #2.写入文件内容
#     f.write("静夜思（李白）\n")
#     f.write("窗前明月光\n")
#     f.write("疑是地上霜\n")
#     f.write("举头望明月\n")
#     f.write("低头思故乡\n")
#
# finally:
#     # 3.关闭文件
#     f.close()



#==================方式二(最佳实践)================================


with open("resources/静夜思.txt","w",encoding="utf-8") as f:
    f.write("静夜思（李白）\n")
    f.write("窗前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")

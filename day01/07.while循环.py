#while循环语句
#计算1—100之间所有偶数的累加之和
num = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        num += i
    i += 1

      print(f"最终结果为{num}")

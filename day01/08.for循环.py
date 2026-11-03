#for循环语句
#计算1-100之间所有奇数之和
num = 0
i = 1
for i in range(100):
    if i % 2 == 1:
        num += i
print(f"1-100之间所有奇数之和为{num}")
#计算100-500之间所有3的倍数的数字之和
num = 0
i = 100
for i in range(100,501):
    if i % 3 == 0:
        num += i
print(f"100-500之间所有3的倍数的数字之和为{num}")

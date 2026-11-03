#递归调用（先层层递进，再层层回归），在函数中自己调用自己的情况（要有终结点）。
#定义一个函数，根据传入的数字，计算该数字阶乘的结果。
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
num = int(input("请输入数字："))
print(factorial(num))


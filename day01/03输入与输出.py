#输入与输出
#小智的英航卡中有10000元，到现在ATM进行取钱操作，请根据输入的金额执行取钱操作，取钱完毕后，展示其银行卡余额
password = 123456
total_amount = 10000
word = int(input("请输入密码："))
if word == password:
    amount = int(input("请输入取款金额:"))
    if amount>total_amount:
        print("余额不足")
    else:
        total_amount = total_amount - amount
        print(f"余额为：{total_amount}")
else:print("密码错误！")


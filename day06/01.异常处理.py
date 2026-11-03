#1.程序运行过程中出现异常，有两种处理方案：
#1.不做处理：整个程序因为一个bug，中断执行（之前编程的程序）
#捕获异常：按照我们自己的处理方式，处理完一场，程序继续执行（编写程序时，做好预案，出现异常，按预备方案处理）
try:
    print("= = = = = = = =")
    print(my_name)
    print(1/0)
    print("ABC"[10])
    print("= = = = = = = =")
except NameError as e:# 捕获具体信息
    print("程序运行报错，错误信息",e)
except ZeroDivisionError as e:
    print("0不能做被除数，异常信息",e)
except IndexError as e:
    print("索引错误，异常信息",e)
except Exception as e:
    print("程序运行出错，错误信息",e)
finally:# 无论程序是否正确运行，finally代码块中的代码都会运行
    print("释放资源")
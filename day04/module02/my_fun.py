# 常量（不会发生变化的数据；常量的名称全部大写）
# __all__ 是一个模块级别的特殊变量，用于指定from 模块名 import * 时会导入哪些功能（*通配的哪些功能）。
__all__ = ["log_separator1","log_separator3","PI"]
PI = 3.1415926
NAME = "凉韵"

def log_separator1():
    print("- " * 30)
def log_separator2():
    print("+ " * 30)
def log_separator3():
    print("# " * 30)
def log_separator4():
    print("* " * 30)

#__name--:Python中内置变量，表示当面模块的名字（直接运行当面模块，__mane__的值为“__main__”;当该模块被导入是，__name__的值就是模块的名称）
# 执行当前文件，则会执行如下代码；如果被当作模块导入，如下代码不执行。
if __name__ == "__main__":
    log_separator1()
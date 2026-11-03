"""
导入形式                             代码样例                                 调用方式          调用方式
import 模块名                        import random，os                       模块名.功能名      random.randint(10,100)
import 模块名 as 别名                 import random as rd                     别名.功能名       rd.randint(10,100)
from 模块名 import 功能名             from random import randint,choice       功能名            randint(10,100)
from 模块名 import 功能名 as 别名      from random import randint as rint      别名              rint(10,100)
from 模块名 import *                 from random import *                    功能名            randint(10,100)
"""
#导入模块----->调用方式：模块名.功能名/别名.功能名
# import random
# import random as rd
# for i in range(100):
#     print(random.randint(1,100))
# for i in range(100):
#     print(rd.randint(1,100))

#导入模块中的功能 from...import...---->调用方式：功能名/别名
# from random import randint
# from random import randint as rint
# from random import randint
# for i in range(100):
#     print(randint(1,100))
# for i in range(100):
#     print(rint(1,100))
# for i in range(100):
#     print(randint(1,100))




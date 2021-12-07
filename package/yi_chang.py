# 异常的处理
# 异常：运行代码过程中的任何错误，带有error字样的都是异常
# 异常处理：我们对代码中所有可能出现的异常，进行处理，因为异常不处理就会导致程
# 序运行终止，而处理可以使代码继续运行下去
# --------语法1：
# try:
#     运行体
# except:
#     捕获之后的处理逻辑

import os

# 异常的捕获
# ------什么异常都捕获
try:
    os.mkdir("test")
except :
    print("这里出现异常了！")

# ------什么异常都捕获
try:
    os.mkdir("test")
# as将报错赋予变量
except Exception as e:
    print("异常信息为{}".format(e))

# ------捕获某一类异常
try:
    os.mkdir("test")
except OSError as e :
    print("异常信息为{}".format(e))

# ------捕获特定的异常，节省资源
# python中必须运行出错之后，才能知道错误是什么，所以如果要抓具体错误，调试抓错
try:
    os.mkdir("test")
except FileExistsError as e :
    print("异常信息为{0}".format(e))

# --------语法2：
# try:
#     运行体
# except:
#     捕获之后的处理逻辑
# finally:#不论是否捕捉，都要执行的逻辑
#     不论是否捕捉，都要执行的逻辑

try:
    os.mkdir("test")
except Exception as e :
    print("异常信息为{0}".format(e))
finally:
    print("我总是会执行")

# --------语法3：
# try:
#     运行体
# except:
#     捕获之后的处理逻辑
# else:
#     捕捉，就不执行；
#     没被捕捉，就执行

try:
    os.mkdir("test")
except Exception as e :
    print("异常信息为{0}".format(e))
else:
    print("我是else")

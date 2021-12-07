# 常用的文件格式：file、txt、xml、html
# -----open函数，打开文件
# 函数的参数列表(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
# -----mode是打开这个文件的模式，默认是r(下面常用的一些模式)：
# r(读写)    w(写)     a(追加)
# r+    w+     a+
# 字节文件
# rb    wb     ab
# rb+    wb+     ab+
# -----encoding 指定编码格式

# ----read
# 1.文件open处理之后，默认只读模式，执行写操作会报错
# 2.r+ 权限，可读可写，读写跟着光标走
# 3.read(int),读取文本前int个字符，并且对于系统而言，读取操作后，光标都会结束在当前读取的最后面
# 4.如果要写入中文，需要注意编码格式
# 5.最好是读写分离

file = open("test","r+")
# # 先写后读，直接从文本开头覆盖文本内容,并且不会被读的行为检测到新写的内容
# # 文本写的操作，返回的数据类型是int
# file.write("mmmm")
# # 因为读写跟着光标走，在文件先执行了写的操作之后，光标到了写完之后的位置，所以读的起点也跟着变化了
# res = file.read()
# print(res)
#
# # 先读后写，文本追加在原文本的末尾，也不会显示出写的内容
# res2 = file.read();
# file.write("mmmm")
# print(res2)
#
# # ----write  不要轻易使用w权限，因为w权限在对文件进行写的操作的时候，是先清空内容再写入内容
# # 1.只写权限，执行读操作会报错
# # 2.w+ 权限，可读可写
# # 3.不论w，还是w+，如果文件存在，则直接清空再重写，如果文件不存在，则新建一个文件，然后在写
#
# # ----apend  推荐使用的写权限，是追加文本末尾的写入逻辑
# # 1.不论w，还是w+，如果文件存在，则直接末尾写入；如果文件不存在，则新建一个文件，然后在写
# file2 = open("test","a+")
# # "\n"换行符
# file2.write("\n我要换行")

# ----readline 默认读取第一行,并且自带换行功能；
# 在同一模块下，出现对同一文件的readline操作时，会递增一行一行的读取下去
# ----readline(int) 可以指定读取文件从开头查起的int个字符,并且自带换行功能
# ----readlines 默认读取文件内的所有文本，以列表形式返回数据

print(file.readline()+"111111")
print(file.readline(2)+"111111")
print(file.readlines())

# ----readlines 默认读取文件内的所有文本，以列表形式返回数据
# ----writelines 对应readlines，writelines写入的传参也是列表数据类型；
# 但是默认追加文本末尾，并且不换行，所以需要在写入的内容上添加换行符
file.writelines(["xxxxxx\n","yyyyyyy"])

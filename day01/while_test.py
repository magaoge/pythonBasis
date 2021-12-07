# while 控制循环
# 语法：
# while 条件表达式：
#     子代码块

# 执行规律：首先判断while后面的条件表达式是否成立
# 如果为TRUE则执行子代码块，执行完毕之后，继续判断，直到不满足条件为止


# 为了防止代码进入死循环:
# 1.在循环过程中添加变量控制循环
# 2.通过break和continue来控制

a = 9

while a < 10 :
    print(a)
    a=a+1
# while 控制循环
# 语法：
# while 条件表达式：
#     子代码块

# 执行规律：首先判断while后面的条件表达式是否成立
# 如果为TRUE则执行子代码块，执行完毕之后，继续判断，直到不满足条件为止


# 为了防止代码进入死循环:
# 1.在循环过程中添加变量控制循环
# 2.通过break和continue来控制

a = 9

while a < 10 :
    print(a)
    a=a+1

while True:
    print(str(a)+"aaaaa")
    a = a - 1
    if a < 0:
        break
    else:
        continue


while True:
    print(str(a)+"aaaaa")
    a = a - 1
    if a < 0:
        break
    else:
        continue


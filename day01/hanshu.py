# -----函数特点：
# 可以重复使用
#
# -----函数的语法：def 关键字
# -----函数的命名规范：小写字母，不能以数字开头，不同的字母之间用下划线隔开
# def 函数名()：
#     函数体：希望实现的函数逻辑
# -----调用：函数名()

def print_key_word():
    print('hello!')

print_key_word()

# ------函数的参数
# -----形参/顺序参数，函数如果有形参，则函数调用时，必须传递参数；
# 形参的数据格式，取决于函数内对参数的引用限制。比如函数内打印参数，那么参数默认数据类型为字符串；如果是算数运算，则默认为数字类型
# 形参的顺序，顺序传参，但是引用不限制顺序，根据参数名来对应
# -----默认参数，函数里是默认参数的时候，函数调用时，参数可传可不传。
# 不传时，函数内的引用，默认引用默认参数；传递时，函数内引用传递的参数
# 注：两种参数可以混合使用，混合使用时，默认参数必须在参数列表中的形参后
def print_key_word_2(key_word):
    print(key_word)

print_key_word_2('x')

def print_key_word_3(key_word=1):
    print(key_word)

print_key_word_3()
print_key_word_3(2)

def print_key_word_4(a,b=1):
    print(a+b)

print_key_word_4(5)

# ----动态参数/不定长参数
# *args,在函数内部体现为一个元祖
def print_key_word_5(*args):
    print(args)

print_key_word_5(5,6,7)

# ----关键字参数
# **kwargs: 函数内数据体现为key-value字典形式
def print_key_word_6(**kwargs):
    print(kwargs)

print_key_word_6(a=1,b=5)

# 形参与其他参数都可以混用
# 混用时形参最好放在参数列表的首位参数
def print_key_word_7(a,**kwargs):
    print(a,kwargs)

print_key_word_7(1,b=5)

def print_key_word_8(a,*args):
    print(a,args)

print_key_word_8(1,5,6,7)

# 形参如果在参数列表的末尾参数，可能造成系统的歧义，所以在末尾(不适用于关键字参数)，函数引用时必须赋予变量值
def print_key_word_7(*args,a):
    print(args,a)

print_key_word_7(1,2,3,a=5)
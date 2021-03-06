# Python 类的语法  关键字：class 类名
# 类名规范：数字、字母、下换线，不能数字开头，首字母大写，驼峰命名
# 类当中包括：类属性、类函数/类方法

# 声明类
class BoyFriend:
    # 类属性
    a = 15
    b= "xy"
    # 类函数
    # self是变量名，是类的对象本身，最好不要改变。
    # 类的对象调用函数时，输出的就是类的内存地址
    # self是固定的占坑符号，类中的函数都必须带self这个参数
    def han(self):
        print(self)
        print(self.b)

# 类的对象/实例
# 类的对象具有类里面所有属性和方法的使用权限
bf = BoyFriend()#现在bf就是对象

# 类属性、函数的调用：对象.函数/属性名
bf.han()

# 若果要在另外一个模块中引用反射，需要引入
from fan_she import GetDate

if __name__ == '__main__':
    setattr(GetDate, "Cookie", "第二个值")
    print(getattr(GetDate, "Cookie"))

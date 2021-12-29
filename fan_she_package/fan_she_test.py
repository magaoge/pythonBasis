# 若果要在另外一个模块中引用反射，需要引入
from fan_she import GetDate

if __name__ == '__main__':
    setattr(GetDate,"Cookie","第一个值")
    print(getattr(GetDate, "Cookie"))

    # 每次引用都是一个新的反射对象
    setattr(GetDate,"Cookie","第二个值")
    print(getattr(GetDate, "Cookie"))

    delattr(GetDate, "Cookie")
    print(hasattr(GetDate, "Cookie"))

    setattr(GetDate,"Cookie","第三个值")
    print(getattr(GetDate, "Cookie"))
    print(hasattr(GetDate, "Cookie"))
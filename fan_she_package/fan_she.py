# 反射
# 注意，反射是与类相关的，不仅限于要单独去做一个反射类，这里反射有点像Java中的实体类
class GetDate:
    Cookie = None

if __name__ == '__main__':
    print(GetDate.Cookie)

    # 反射中用到的方法
    # 1.设置属性值
    print(setattr(GetDate,"Cookie","小黄"))
    # 2.判断类中是否有该变量
    print(hasattr(GetDate, "Cookie"))
    # 3.获取变量值
    print(getattr(GetDate, "Cookie"))
    # 4.删除变量
    delattr(GetDate, "Cookie")

    print(hasattr(GetDate, "Cookie"))
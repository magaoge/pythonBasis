# ddt+unittest来进行数据的处理
# 装饰器：@+装饰器名，会在装饰的函数前运行
import unittest

from ddt import ddt,data,unpack

data_list = [1,2]

data_in_list = [[1, 2], [3, 4, 5],[6,7]]

dict_list = [{'name':'小红','age':12},{'name':'小绿','age':20}]

@ddt#装饰测试类，标明需要传入数据的类
class DDT(unittest.TestCase):

    @data(data_list)#装饰测试方法，标明需要传入的数据源
    def test_print_data(self,a):
        print(a)
    #
    @data(*data_list)#*号脱衣符，只可脱一层
    def test_print_data1(self,a):
        print(a)

    # @data(*data_list)
    # @unpack#将传入的参数拆分
    # # 注：
    # # 1.unpack将参数拆分传入之后，我们case用例方法就可以传入参数了，但是要注意参数数量的对应
    # # 2.unpack不建议使用，因为拆分出的数据多的时候，参数也要对应传递很多，建议5个以下使用；而且对于数据格式也有要求，详例：test_print_data3
    def test_print_data2(self,a,b):
        print(a)
        print(b)

    @data(data_in_list)
    @unpack#将传入的参数拆分
    def test_print_data3(self,a,b):
        print(a)
        print(b)

    @data(*data_in_list)
    @unpack#将传入的参数拆分
    def test_print_data4(self,a=None,b=None,c=None):
        print(a)
        print(b)
        print(c)

    # 但是上一种方法，参数一旦躲起来依旧是很不方便的操作方式，我们可以根据索引取值
    @data(*data_in_list)
    def test_print_data5(self,a):
        for i in range(0,len(a)):
            print(a[i])

# 对于字典的处理方法有两种：
# 第一种：
    @data(*dict_list)
    def test_print_data6(self,a):
        print(a['name'])
        print(a['age'])

# 第二种：结合unpack
    @data(*dict_list)
    @unpack
    def test_print_data7(self,name,age):
        print(name)
        print(age)

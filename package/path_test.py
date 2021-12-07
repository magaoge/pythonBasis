# -------路径
# 绝对路径     绝对路径   不懂的真的要去百度了，不想记录了

# -------路径获取
import os

# 获取当前所在路径
path = os.getcwd()
print(path)
# 获取当前模块的全路径（包含文件名）
path2 = os.path.realpath(__file__)
print(path2)
# 获取当前模块名
path3 = os.path.relpath(__file__)
print(path3)

# ------路径拼接
# 关键字：os.path.join这种方法不需要添加反斜杠
# 并且可以传不定长参数，但是必须保证父级目录都存在

# 注：拼接之后也只是字符串，还是需要调用os.mkdir()函数进行文件夹创建

new_path = os.path.join(os.getcwd(),"test_father","test_sun")
print(new_path)

new_path = os.getcwd()+"\\test"
print(new_path)

# -------判断是文件还是目录
print(os.path.isfile(os.getcwd()))
print(os.path.isdir(os.getcwd()))

# -------判断文件、文件夹是否存在
print(os.path.exists(os.getcwd()))
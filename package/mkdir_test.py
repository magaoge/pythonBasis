

# --------新建文件夹
# 关键字：os.mkdir("文件夹名")
# 注：如果只是相对路径，生成的文件夹，默认与该模块在同一目录下；当然也可以写绝对路径来生成文件夹
import os

os.mkdir("test")

# --------新建多级文件夹
# 注：必须保证父级目录已经存在；使用"/"来分级
# python转义符自己百度学习
os.mkdir("test/test2")

# --------删除文件夹
# 删除文件也是一级一级删除的，如果直接删除父级文件夹，系统报错
# os.rmdir("test")

# os.rmdir("test/test2")
# os.rmdir("test")

# 罗列出当前路径的所有文件和目录
# os.listdir()返回的数据类型是列表类型
print(os.listdir(os.getcwd()))


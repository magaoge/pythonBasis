# -----------for 循环语法 ：
# for 变量名 in 数据类型x :
#         print(变量名)
# Python通过缩进来控制子集关系
# 相当于是循环遍历x中的元素，赋值给变量名，然后输出变量名
# 循环的次数取决于数据类型的长度
# 注：对于字典类型的数据，循环赋值的是k的值

a = {"class": "a1",
     "student": 111,
     "teacher": "ma",
     "age": "12",
     "score":[1,2,3]};

for i in a :
    print(i)
    print(a[i])

# 字典.keys()函数，获取字典所有的key，返回数据类型是<class 'dict_keys'>
# 字典.values()函数，获取字典所有的value，返回数据类型是<class 'dict_values'>
print(a.keys())
print(type(a.keys()))
print(type(a.values()))
print(a.values())

# range()函数，生成整数序列
# range(m,n,k)m是头，默认0开始，n是尾，k是步长，步长默认为1，取头不取尾
for i in range(1,10) :
    for j in range(1,i+1) :
        print("{}*{}={}".format(j,i,j*i),end=" ")
    print("")
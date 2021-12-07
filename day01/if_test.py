# 控制语句 作用：分值分流 if 循环语句：for ，while
# ---------判断语句1 if 关键字
# 注意：
# 1.if 条件语句（比较、逻辑、成员运算、均可）
# 2.字符串、列表、元祖、字典的空数据，都是false，非空数据都是ture
s = 'x';
m ='';
if s :
    print('执行！')
if m :
    print('不执行！')
# 3.直接通过true或者false来控制if语句的执行

# ---------判断语句2 if...else... 关键字
# 注：else后面不加条件判断语句
age = 18;

if age>=18:
    print('成年')
else:
    print('未成年')

# ---------判断语句3 if...elif...else... 关键字
# elif可以加多个

age = 18

if age > 18:
    print('成年')
elif age < 18:
    print('未成年')
else:
    print('age = 18')

# input():输入函数，输入之后，函数返回值为str
age = int(input('请输入你的年龄：'))
print(age)

# import函数，引入类
# random(): 随机函数
# randint(开始值，结束值)：random()函数的方法，限定随机数字的范围，两边都包含
import random;
age = random.randint(1,9)
print(age)
inputValue = int(input('请输入你的数字：'))

if inputValue == age :
    print('猜对了')
else :
    print('猜错了')

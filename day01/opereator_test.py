# 运算符 5大类：
# -------算数运算符：+ — * / %
# -------赋值运算符：= += -=
# ------比较运算符：>,<,>=,<=,!=,== 6种关系，返回比较结果是布尔值
print("get"=="GET")
# 小写变大写的函数
print("get".upper()=="GET")
# 大写变小写的函数
print("get"=="GET".lower())

# ------逻辑运算符：and or not
# ------逻辑运算符的返回结果是布尔值 True false
# and 需要两边都为真，真真为

# -------成员运算符 in ，not in
a = [1,0.1,'hello',[1,2,3],True];
print(1 in a);
# 对于字典的判断，是判断k是否存在
a = {"class": "a1",
     "student": 111,
     "teacher": "ma",
     "age": "12",
     "score":[1,2,3]};
print("age" in a);
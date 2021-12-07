# 需要导入的依赖，如何安装依赖，查看之前的笔记，或者百度
# 注：这里可能只装一个依赖是不可以的，如果因为缺少依赖而运行失败，报错会提示
import requests

# 接口可以在聚合数据中找免费的接口
url = "https://v.juhe.cn/laohuangli/d"
# 参数传参在python代码中，统一做字符串处理
data = {'key':'b53877420fb1fa596113be1e48065d0a','date':'2014-09-09'}


# --------get
# --------无论什么请求（post或者get，或者其他请求方式）都有两种写法
# requests.get(url, params=None, **kwargs)
# requests.request(method, url, **kwargs)，这里的重点是，一定要用params=data声明关键字传参
# 两种方法都可以将参数在url携带,或者单独携带
# 返回的都是是一个完整的请求（包含响应头、响应体、响应状态）
res = requests.get(url,data)
res = requests.request("GET",url,params=data)

print(res)#但是直接输出的话，只是接口的响应状态

# 响应头
print(res.headers)
# 响应状态
print(res.status_code)
# 响应报文
# text将返回信息以文本展示，数据类型是str，并且支持所有的响应报文数据格式（html、xml、json）
print(res.text)
# 将返回信息以json展示，数据类型是dict，但是只支持json类型的数据格式，推荐使用，json()，方便后期处理取值
print(res.json())

# --------------------post请求方式的接口，几乎和get一样,在请求部分的代码,也是有两种写法
url = "https://v.juhe.cn/laohuangli/d"

data = {'key':'b53877420fb1fa596113be1e48065d0a','date':'2014-09-09'}
# 这里是可以自定义请求头中的请求来源,伪装自己的请求设备
head = {'User-Agent':'Mozilla/5.0'}

# 首先获取到cookie
res = requests.post(url,data,headers=head)
# 再将cookie作为请求的参数,这里还加入了head参数
res = requests.post(url,data,cookies= res.cookies,headers=head)

# 获取请求头
print(res.request.headers)

print(res)#但是直接输出的话，只是接口的响应状态

# 响应头
print(res.headers)
# 响应状态
print(res.status_code)
# 响应报文
# text将返回信息以文本展示，数据类型是str，并且支持所有的响应报文数据格式（html、xml、json）
print(res.text)
# 将返回信息以json展示，数据类型是dict，但是只支持json类型的数据格式，推荐使用，json()，方便后期处理取值
print(res.json())
# cookies,一般是登陆的时候，给用户设置的，这里我理解应该是我们在聚合数据中的cookie
# 数据类型是类字典形式，也就是不完全是字典
print(res.cookies)


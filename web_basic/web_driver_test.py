
# coding=gbk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 声明浏览器驱动位置
from selenium.webdriver.common.by import By

s = Service(executable_path = r"D:\project_python\pythonBasis\resource\chromedriver.exe")
# 启动浏览器，开启会话
driver = webdriver.Chrome(service = s)


# 窗口最大化
driver.maximize_window()

# 访问网页
driver.get("http://www.baidu.com")

# ---------------通过id获取元素
# 注：无论是element还是elements，By=ID的时候，返回的都是一个值，而不是一个列表
ele = driver.find_element_by_id("kw")
# 下面是当前版本selenium的封装函数。不过我们学习还是跟着老版本走，只是会有一些error级别的报错，并不影响我们学习
# ele = driver.find_element(by=By.ID,value="kw")

print(ele)

# 通过获取到的元素，来获取元素指定的属性值
print(ele.get_attribute("class"))


# ---------------通过id获取元素
# 注：无论是element还是elements，By=ID的时候，返回的都是一个值，而不是一个列表
ele = driver.find_element_by_id("kw")

# # 访问下一个网页
# # driver.get("http://www.taobao.com")
# # 放回上一个访问页面
# driver.back()
# # 跳至下一个页面
# driver.forward()
# # 刷新页面
# driver.refresh()
#
# # 获取标题
# print(driver.title)
#
# # 获取网址
# print(driver.current_url)
# # 获取窗口句柄
# print(driver.current_window_handle)

# 结束会话，退出浏览器
driver.quit()


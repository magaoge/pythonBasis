
# coding=gbk
from selenium import webdriver

# 启动浏览器，开启会话
driver = webdriver.Chrome(r"D:\project_python\pythonBasis\resource\chromedriver.exe")


# 窗口最大化
driver.maximize_window()

# 访问网页
driver.get("http://www.baidu.com")



driver.close()
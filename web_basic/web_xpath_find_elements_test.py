
# coding=gbk
from selenium import webdriver

# ����������������Ự
driver = webdriver.Chrome(r"D:\project_python\pythonBasis\resource\chromedriver.exe")


# �������
driver.maximize_window()

# ������ҳ
driver.get("http://www.baidu.com")



driver.close()
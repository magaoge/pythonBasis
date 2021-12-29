
# coding=gbk
from selenium import webdriver

# 启动浏览器，开启会话
driver = webdriver.Chrome(r"D:\project_python\pythonBasis\resource\chromedriver.exe")


# 窗口最大化
driver.maximize_window()

# 访问网页
driver.get("http://www.baidu.com")

# ---------------通过id获取元素
# 注：无论是element还是elements，By=ID的时候，返回的都是一个值，而不是一个列表
ele = driver.find_element_by_id("kw")
# 下面是当前版本selenium的封装函数。不过我们学习还是跟着老版本走，只是会有一些error级别的报错，并不影响我们学习
# ele = driver.find_element(by=By.ID,value="kw")
print(ele)# 获取的是一个WebElement对象
print(ele.text)# 输出对象文本值，只对有文本的元素生效
# ------------通过获取到的元素，来获取元素指定的属性值
print(ele.get_attribute("class"))


# ---------------通过class获取元素
# 注：element获取的是页面元素匹配到的第一个值
ele2 = driver.find_element_by_class_name("s_ipt")
print(ele2)
# 注：elements获取的是页面元素所有匹配到的元素对象，返回值类型是列表
ele_list = driver.find_elements_by_class_name("s_ipt")
print(ele_list)

# ---------------通过name获取元素
ele3 = driver.find_element_by_name("wd")
print(ele3)
name_ele_list = driver.find_elements_by_name("wd")
print(name_ele_list)

# ---------------通过tagname获取元素
ele4 = driver.find_element_by_tag_name("input")
print(ele4)
tag_ele_list = driver.find_elements_by_tag_name("input")
print(tag_ele_list)

# ---------------通过文本定位
# 精准匹配
ele5 = driver.find_element_by_link_text("图片")
print(ele5.text)
text_ele_list = driver.find_elements_by_link_text("图片")
print(ele5.text)
# 模糊匹配
ele6 = driver.find_element_by_partial_link_text("图")
print(ele6)
text_ele_list2 = driver.find_elements_by_partial_link_text("图")
print(text_ele_list2)


driver.close()
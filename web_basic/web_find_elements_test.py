
# coding=gbk
from selenium import webdriver

# ����������������Ự
driver = webdriver.Chrome(r"D:\project_python\pythonBasis\resource\chromedriver.exe")


# �������
driver.maximize_window()

# ������ҳ
driver.get("http://www.baidu.com")

# ---------------ͨ��id��ȡԪ��
# ע��������element����elements��By=ID��ʱ�򣬷��صĶ���һ��ֵ��������һ���б�
ele = driver.find_element_by_id("kw")
# �����ǵ�ǰ�汾selenium�ķ�װ��������������ѧϰ���Ǹ����ϰ汾�ߣ�ֻ�ǻ���һЩerror����ı�������Ӱ������ѧϰ
# ele = driver.find_element(by=By.ID,value="kw")
print(ele)# ��ȡ����һ��WebElement����
print(ele.text)# ��������ı�ֵ��ֻ�����ı���Ԫ����Ч
# ------------ͨ����ȡ����Ԫ�أ�����ȡԪ��ָ��������ֵ
print(ele.get_attribute("class"))


# ---------------ͨ��class��ȡԪ��
# ע��element��ȡ����ҳ��Ԫ��ƥ�䵽�ĵ�һ��ֵ
ele2 = driver.find_element_by_class_name("s_ipt")
print(ele2)
# ע��elements��ȡ����ҳ��Ԫ������ƥ�䵽��Ԫ�ض��󣬷���ֵ�������б�
ele_list = driver.find_elements_by_class_name("s_ipt")
print(ele_list)

# ---------------ͨ��name��ȡԪ��
ele3 = driver.find_element_by_name("wd")
print(ele3)
name_ele_list = driver.find_elements_by_name("wd")
print(name_ele_list)

# ---------------ͨ��tagname��ȡԪ��
ele4 = driver.find_element_by_tag_name("input")
print(ele4)
tag_ele_list = driver.find_elements_by_tag_name("input")
print(tag_ele_list)

# ---------------ͨ���ı���λ
# ��׼ƥ��
ele5 = driver.find_element_by_link_text("ͼƬ")
print(ele5.text)
text_ele_list = driver.find_elements_by_link_text("ͼƬ")
print(ele5.text)
# ģ��ƥ��
ele6 = driver.find_element_by_partial_link_text("ͼ")
print(ele6)
text_ele_list2 = driver.find_elements_by_partial_link_text("ͼ")
print(text_ele_list2)


driver.close()

# coding=gbk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# �������������λ��
from selenium.webdriver.common.by import By

s = Service(executable_path = r"D:\project_python\pythonBasis\resource\chromedriver.exe")
# ����������������Ự
driver = webdriver.Chrome(service = s)


# �������
driver.maximize_window()

# ������ҳ
driver.get("http://www.baidu.com")

# ---------------ͨ��id��ȡԪ��
# ע��������element����elements��By=ID��ʱ�򣬷��صĶ���һ��ֵ��������һ���б�
ele = driver.find_element_by_id("kw")
# �����ǵ�ǰ�汾selenium�ķ�װ��������������ѧϰ���Ǹ����ϰ汾�ߣ�ֻ�ǻ���һЩerror����ı�������Ӱ������ѧϰ
# ele = driver.find_element(by=By.ID,value="kw")

print(ele)

# ͨ����ȡ����Ԫ�أ�����ȡԪ��ָ��������ֵ
print(ele.get_attribute("class"))


# ---------------ͨ��id��ȡԪ��
# ע��������element����elements��By=ID��ʱ�򣬷��صĶ���һ��ֵ��������һ���б�
ele = driver.find_element_by_id("kw")

# # ������һ����ҳ
# # driver.get("http://www.taobao.com")
# # �Ż���һ������ҳ��
# driver.back()
# # ������һ��ҳ��
# driver.forward()
# # ˢ��ҳ��
# driver.refresh()
#
# # ��ȡ����
# print(driver.title)
#
# # ��ȡ��ַ
# print(driver.current_url)
# # ��ȡ���ھ��
# print(driver.current_window_handle)

# �����Ự���˳������
driver.quit()


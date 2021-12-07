import unittest
from jie_kou_test.test_case import CaseTest
from jie_kou_test.do_excel import DoExcel

import haohan_HTMLTestRunner

data = DoExcel("python.xlsx","test").do_excel()
print(data)

suit = unittest.TestSuite()

loader = unittest.TestLoader
for item in data:
    suit.addTest(CaseTest("test_city",item["method"],item["url"],item["data"]))
#     suit.addTest(CaseTest("test_city",url,data[0]))

# with open("report.txt","w+",encoding="UTF-8") as file:
#     runner = unittest.TextTestRunner(stream=file,verbosity=2)
#     runner.run(suit)

with open("api_test.html","wb") as file:
    runner = haohan_HTMLTestRunner.HTMLTestRunner(stream=file,  #报告输出文件对象
                                                  verbosity=2,  #报告详细级别
                                                  title="magaoge 的 haohan 测试报告",  #报告标题
                                                  description="第一份测试报告",  #报告描述
                                                  tester="magaoge")#测试人
    runner.run(suit)
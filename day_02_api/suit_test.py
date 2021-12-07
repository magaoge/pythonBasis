import unittest
import haohan_HTMLTestRunner

from day_02_api import test_case
from test_case import CaseTest
from do_Excel import DoExcel

suit = unittest.TestSuite()

loader = unittest.TestLoader()
suit.addTest(loader.loadTestsFromTestCase(CaseTest))

with open("api_test.html","wb") as file:
    runner = haohan_HTMLTestRunner.HTMLTestRunner(stream=file,#报告输出文件对象
                                                   verbosity=2,#报告详细级别
                                                   title="magaoge 的 haohan 测试报告",#报告标题
                                                   description="第一份测试报告",#报告描述
                                                   tester="magaoge")#测试人
    runner.run(suit)


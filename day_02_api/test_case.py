import unittest
from api_request import WeatherAPI
from ddt import ddt,data,unpack

# url = "http://apis.juhe.cn/simpleWeather/query"
# data = {"city": "上海", "key": "f429afefae31a7f4912f68f962535d1d"}
from day_02_api.do_Excel import DoExcel

data_list = DoExcel("python.xlsx","test").do_excel()
# print(data_list)

@ddt
class CaseTest(unittest.TestCase):

    @data(*data_list)
    # @unpack
    def test_city(self,item):
        wa = WeatherAPI()
        res = wa.queryWeather(item['method'],item['url'],item['data'])
        print(res.text)
        try:
            self.assertEqual("查询成功!",res.json()["reason"],"*********{}**********不是我们期望的值！".format(res.json()["reason"]))
        except AssertionError as e:
            print("test_city's error is{}".format(e))
            raise


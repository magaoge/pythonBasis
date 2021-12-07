import unittest
from jie_kou_test.jie_kou import WeatherAPI

# url = "http://apis.juhe.cn/simpleWeather/query"
# data = {"city": "上海", "key": "f429afefae31a7f4912f68f962535d1d"}


class CaseTest(unittest.TestCase):

    def __init__(self,methodName,method,url,data):
        super(CaseTest, self).__init__(methodName)
        self.url = url
        self.data = data
        self.method = method

    def test_city(self):
        wa = WeatherAPI()
        res = wa.queryWeather(self.method,self.url,self.data)
        print(res.text)
        try:
            self.assertEqual("查询成功!",res.json()["reason"],"*********{}**********不是我们期望的值！".format(res.json()["reason"]))
        except AssertionError as e:
            print("test_city's error is{}".format(e))
            raise
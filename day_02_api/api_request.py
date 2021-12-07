import requests

url = "http://apis.juhe.cn/simpleWeather/query"
# data = {"city": "上海", "key": "f429afefae31a7f4912f68f962535d1d"}
# data = [{"data":{"city": "上海", "key": "f429afefae31a7f4912f68f962535d1d"}}
#         ,{"data":{"city": "北京", "key": "f429afefae31a7f4912f68f962535d1d"}}
#         ,{"data":{"city": "南京", "key": "f429afefae31a7f4912f68f962535d1d"}}]

class WeatherAPI:

    def queryWeather(self,method,url,data):
        res = requests.request(method, url, params=data, verify=False)

        # print(url+"---------------"+str(data))
        # print(res.status_code)
        # print(res.headers)
        print('json：'+str(res.json()))

        return res

# if __name__ == '__main__':
#
#     wa = WeatherAPI()
#     wa.queryWeather(url, data[0]["data"])
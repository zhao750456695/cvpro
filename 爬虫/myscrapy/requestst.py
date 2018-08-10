# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/4/6 11:35'
import requests
import json
# response=requests.get('https://www.baidu.com')
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.text)
# print(response.cookies)
#
# requests.post('http://httpbin.org/post')
# requests.put('http://httpbin.org/put')
# requests.delete('http://httpbin.org/delete')
# requests.head('http://httpbin.org/get')
# requests.options('http://httpbin.org/get')

# response=requests.get('http://httpbin.org/get?name=germ&age=22')
# print(response.text)

# data={
#     'name': 'germ',
#     'age': 22
# }
# response=requests.get('http://httpbin.org/get', params=data)
# print(response.text)
#
# response=requests.get('http://httpbin.org/get')
# print(type(response.text))
# print(json.loads(response.text))
# print(response.json())
# print(type(response.json()))

# response=requests.get('https://github.com/favicon.ico')
# print(type(response.text), type(response.content))
# print(response.text)
# print(response.content)
#
# with open('./favicon.ico', 'wb') as f:
#     f.write(response.content)
#     f.close()


# headers={
#      'User-Agent':  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#  }
# response=requests.get('https://www.zhihu.com/explore', headers=headers)
# print(response.text)
#
# data={
#     'name': 'germ',
#     'age': 22
# }
# response=requests.post('http://httpbin.org/post', data=data, headers=headers)
# print(response.text)

#
# response=requests.get('http://www.jianshu.com')
# print(type(response.status_code), response.status_code)
# print(type(response.headers), response.headers)
# print(type(response.cookies), response.cookies)
# print(type(response.url), response.url)
# print(type(response.history), response.history)


# response=requests.get('http://jianshu.com')
# exit() if not response.status_code == requests.codes.ok else print('Request Successfully')

# files={
#     'files': open('./favicon.ico', 'rb')
# }
# response=requests.post('http://httpbin.org/post', files=files)
# print(response.text)

# response=requests.get('http://www.baidu.com')
# print(response.cookies)
# for key, value in response.cookies.items():
#     print(key+'='+value)
#
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# response=requests.get('http://httpbin.org/cookies')
# print(response.text)
#
# from requests.packages import urllib3
# urllib3.disable_warnings()
# response=requests.get('https://www.12306.cn', cert=)
# print(response.status_code)

proxies={
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
}
response=requests.get('https://www.taobao.com', proxies=proxies)
print(response.status_code)
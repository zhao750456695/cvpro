# ========== IP代理
import requests

proxy = '127.0.0.1:8888'
# 需要认证的代理
# proxy = 'username:password@127.0.0.1:8888'
url =  'http://httpbin.org/get'
proxies ={
	'http': 'http://' + proxy,
	'https': 'https://' + proxy,
}
try:
	response = requests.get(url , proxies=proxies)
	print(response.text)
except requests.exceptions.ConnectionError as e:
	print('Error', e.args)
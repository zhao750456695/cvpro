# IP代理
from selenium import webdriver

service_args =[
    '--proxy=127.0.0.1:9743',
	'--proxy-type=http',
	#'--proxy-auth=username:password' # 带认证代理
]

browser = webdriver.PhantomJS(service_args=service_args)
browser.get('http://httpbin.rog/get')
print(browser.page_source)

# IP代理
from selenium import webdriver
# 要将chromewebdriver放在当前路径下
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://'+proxy)
chrome = webdriver.Chrome(chrome_options=chrome_options)
chrome.get('http://httpbin.org/get')

print(chrome.page_source)




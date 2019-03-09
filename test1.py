# request:GET
# import urllib.request
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))


# request: POST
# http测试：http://httpbin.org/
# import urllib.parse
# import urllib.request
# data = bytes(urllib.parse.urlencode({'word':"hello"}),encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())

# 超时设置
# import urllib.request
# reponse = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
# print(reponse.read())


# import socket
# import urllib.request
# import urllib.error
#
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('Time Out')

# from urllib.parse import urlparse
# result = urlparse("https://edu.hellobi.com/course/157/play/lesson/2580")
# print(result)


# from urllib.parse import urlunparse
# data = ['http','www.baidu.com','index.html','user','a=6','comment']
# print(urlunparse(data))


# import requests
# response = requests.get("http://www.baidu.com")
# print(response.cookies)
# for key,value in response.cookies.items():
#     print(key + '=' + value)

# import requests
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)

import requests
result = requests.post("http://www.baidu.com")
result.encoding='utf-8'
print(result.text)
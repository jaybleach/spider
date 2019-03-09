# import re
# content = 'Hello 123 4567 world_this is a regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
# print(result)
# print(result.group())
# print(result.span())


# import re
# content = 'Hello 123 4568 world_this is a regex Demo'
# result=re.match('^Hello.*Demo$',content)
# print(result)
# print(result.group())
# print(result.span())


# import re
# content = 'Hello 1234568 world_this is a regex Demo'
# result = re.match('^Hello\s(\d+)\sworld(\w+).*Demo$',content)
# print(result)
# print(result.group(2))
# print(result.span())

# import re
# content = '''Hello 1234568 world_this
# is a regex Demo'''
# result = re.match('^He.*?(\d+).*?Demo$',content,re.S)
# print(result)
# print(result.group(1))
# print(result.span())


# import re
# content = 'price is $5.00'
# result = re.match('price is \$5\.00',content)
# print(result)

# import re
# content = 'Extra stings Hello 1234567 world_this is regex demo extra stings'
# result = re.search('Hello.*?(\d+).*?demo',content)
# print(result)
# print(result.group(1))

#邮箱正则
# import re
# text = input("Please input your Email address：\n")
# if re.match(r'[0-9a-zA-Z_-]{0,19}@(\w+).com',text):
#     print('Email address is Right!')
# else:
#     print('Please reset your right Email address!')

import requests
import re
content = requests.get('http://book.douban.com/').text
# pattern = re.compile('<li.*?cover.*?href="(.*?)".*?class="more-meta"*?title.*?>(.*?)</h4>.*?author.*?>(.*?)</span>.*?year.*?>(.*?)</span>.*?</li>', re.S)
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?</li>', re.S)
results = re.findall(pattern, content)
for result in results:
    url = result
    # author = re.sub('\s', '', author)
    # date = re.sub('\s', '', date)
    print(url)
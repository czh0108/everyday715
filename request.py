import requests
from pprint import pprint
r=requests.get('https://www.qq.com')    #腾讯首页
pprint(r.status_code)   #打印状态码
#200
pprint(r.text)

'''对于带参数的URL，传入一个dict作为params参数：'''
r1=requests.get('https://www.qq.com/search',
                parmas={'q':'python','cat':'1001'}
                )
print(r1.url)   #打印实际请求的URL
#'https://www.qq.com/search?q=python&cat=1001'
print(r1.encoding)
'utf-8'

'''无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：'''
pprint(r.content)

'''对于特定类型的响应，例如JSON，可以直接获取：'''
r2 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
pprint(r2.json())

'''需要传入HTTP Header时，我们传入一个dict作为headers参数：'''
r3 = requests.get('https://www.douban.com/',
                 headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r3.text)
r = requests.get('https://www.douban.com/') # 豆瓣首页
'''请求时，提供一个headers，现在大部分网站都增加了安全验证'''
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://www.douban.com/'
r = requests.get(url, headers=headers)

'''要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：'''
r4=requests.post('https://accounts.douban.com/login',
                data={'form_email': 'abc@example.com', 'form_password': '123456'})

'''requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：'''
params = {'key': 'value'}
r5 = requests.post('url', json=params) # 内部自动序列化为JSON

'''类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：'''
upload_files = {'file': open('report.xls', 'rb')}
r6= requests.post('url', files=upload_files)
#在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
#把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。

'''获取响应头'''
pprint('r.headers')
pprint(r.headers['Content-Type'])

'''requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：'''
r.cookies['ts']
#'example_cookie_12345'
'''要在请求中传入Cookie，只需准备一个dict传入cookies参数：'''
cs = {'token': '12345', 'status': 'working'}
r7= requests.get('url', cookies=cs)

'''要指定超时，传入以秒为单位的timeout参数：'''
r8= requests.get('url', timeout=2.5) # 2.5秒后超时


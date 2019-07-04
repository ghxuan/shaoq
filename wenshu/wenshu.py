import execjs
import requests

# html = requests.get('http://shaoq.com/wenshu')
# print(html.text)

res = execjs.compile(open('1.js', 'r+').read())
url = res.call('f')
print(url)
# html = requests.get(f'http://shaoq.com{url["0"]}')
# print(html.text)

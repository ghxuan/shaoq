import re
import execjs
import requests


def wenshu():
    headers = {
        'Cookie': 'cookie=""',
    }
    html = requests.get('http://shaoq.com/wenshu', headers=headers)
    cookie = dict(i.split('=', 1) for i in html.headers['Set-Cookie'].split('; ')).get('cookie')
    headers['Cookie'] = f'cookie={cookie}'
    res = re.search(r"0 dynamicurl=.*?;0 wzwsquestion=.*?;0 wzwsfactor=.*?;0 wzwsmethod=.*?;0 wzwsparams=.*?;",
                    html.text)
    if res:
        res = res.group()
    else:
        raise ValueError('html格式不对，请检查')
    # print(res)
    cur = execjs.compile(open('1.js', 'r+').read())
    url = cur.call('f', res)['0']
    # print(url)
    html = requests.get('http://shaoq.com' + url,
                        headers=headers)
    return html.text


print(wenshu())

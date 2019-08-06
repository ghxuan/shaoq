import re
import requests


def getip():
    info = requests.get('http://shaoq.com/ip').text
    res = re.search('<head>(.*?)</head>', info, re.S).group(1)
    keys = re.findall(r'\.(.*?){display:none}', res)
    res = re.search('<body>(.*?)<body>', info, re.S).group(1)
    print(r'|'.join([f'(<.*? class="{k}">.*?</.*?>)' for k in keys]) + r'|(<.*? style="display:none">.*?</.*?>)')
    res = re.sub(
        r'|'.join([f'(<.*? class="{k}">.*?</.*?>)' for k in keys]) + r'|(<.*? style="display:none">.*?</.*?>)',
        '', res.split('<br>', 1)[-1])
    res = re.sub(
        r'<.*?>(.*?)</.*?>',
        r'\1', res)
    res = res.replace('\n', '').split('<br>')
    print(res, len(res))


getip()

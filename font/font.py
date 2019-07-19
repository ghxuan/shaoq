from ftc import FTC

import requests
import re


def get_need_k():
    info = requests.get('http://shaoq.com/font').text
    url = re.search(r'src:url\("(static/fonts/.*?\.woff)"\)', info)
    # print(f'http://shaoq.com/{url.groups()[0]}')
    font = requests.get(f'http://shaoq.com/{url.groups()[0]}').content
    with open('shaoq.woff', 'wb+') as f:
        f.write(font)
    info = re.sub(r'&#x(.*?);', r'uni\1', info)
    font_to_value = FTC().ret_key_font()

    print(''.join(font_to_value.get(i, ' ') if 'uni' in i else i for i in
                  re.findall(r'<e.*?>(.*?)</e>', info)))


get_need_k()

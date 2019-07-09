import re
from fontTools.ttLib import TTFont


def get():
    font = TTFont('shaoq.woff')
    base_font = TTFont('microsoft-yahei.woff')
    # print(dir(font['glyf']['unie3ce']))
    print(font['glyf']['unie3ce'])
    with open('font.html', 'r+', encoding='utf-8') as f:
        info = f.read().replace('', '')
    strings = re.findall(r'<e.*?>(.*?)</e>', info)
    print(''.join(strings))


get()

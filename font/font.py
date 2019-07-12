import re


# from fontTools.ttLib import TTFont


def get_need_k():
    with open('font.html', 'r+', encoding='utf-8') as f:
        info = f.read().replace('', '')
    info = re.sub(r'&#x(.*?);', r'uni\1', info)
    font_to_value = dict((f'uni{i}', '') for i in re.findall(r'<e.*?>(uni.*?)</e>', info))

    font_to_value = {
        'unief2d': '真', 'unie313': '好', 'unif3d8': '朋', 'unieee0': '友', 'unif513': '我', 'unif009': '一', 'unif0fa': '对',
        'unieeea': '珠', 'unieb96': '放', 'unief35': '在', 'unif8a7': '个', 'unif755': '的', 'unie6dc': '成', 'uniea24': '子',
        'unif39e': '里', 'unie0a5': '内', 'unif495': '还', 'unieb26': '有', 'unif482': '干', 'unie963': '那', 'unie8dd': '是',
        'unie544': '小', 'unie985': '儿', 'unief4a': '适', 'unif4f2': '又', 'unieeb2': '人', 'unif1a0': '说', 'unif83d': '这',
        'unif857': '种', 'uniedf6': '窗', 'uniea3e': '前', 'unieb93': '大', 'unif2b5': '常', 'unie920': '盛', 'uniebb6': '国',
        'unie36c': '兰', 'unie216': '便', 'unif2cd': '用', 'unie29b': '长', 'unif002': '串', 'unie816': '生', 'uniee1a': '着',
        'unie3ce': '上', 'unie9bd': '们', 'uniefa9': '就', 'unie3cb': '像', 'unie5fc': '进', 'uniede5': '林', 'unif042': '样',
        'unie579': '安', 'unie8b0': '全', 'unif5da': '中', 'uniefff': '出', 'unie92f': '般', 'unif3d9': '也', 'unif720': '格',
        'unif6f4': '外', 'unie66d': '松', 'unie8d5': '自', 'unie746': '了', 'uniec94': '阳', 'unieede': '光', 'unif435': '入',
        'unie77a': '过', 'unie54b': '些', 'unie0d8': '无', 'unief3c': '甲', 'uniecdc': '影', 'unie63b': '如', 'unie06d': '同',
        'unif134': '玉', 'unif173': '意', 'unif571': '间', 'unie4f8': '动', 'uniea2b': '看', 'unie689': '不', 'unif22a': '完',
        'unie285': '整', 'unif740': '时', 'unief3d': '连', 'unie0e0': '可', 'unif762': '爱', 'unie847': '鲜', 'uniee0c': '红',
        'unie060': '来', 'unie5bd': '很', 'unie49d': '少', 'unie70a': '开', 'unie6f5': '点', 'unix': ' ', 'unie37d': '三',
        'uniee48': '后', 'unie830': '团', 'unif735': '发', 'unie51e': '边', 'unief83': '嫩', 'unif754': '到', 'unif35f': '片',
        'unie4d5': '食', 'unie13a': '加', 'unif888': '水', 'unieff3': '去', 'unie3e1': '多', 'unif113': '然', 'unie2f7': '更',
        'unief5d': '正', 'uniebb5': '家', 'unif5f0': '能', 'uniea28': '地', 'unie421': '么', 'uniecf7': '色', 'unif8c2': '只',
        'unie4f6': '没', 'unif591': '白', 'unif417': '起', 'unif3ce': '四', 'unie6ce': '周', 'unif53e': '活', 'uniee3e': '屋',
        'unif60f': '会', 'unie5be': '气', 'unif7e9': '十', 'unie9ec': '足', 'unie038': '站', 'uniee9a': '文', 'unif3a4': '名',
        'unie60c': '字', 'unie78f': '得', 'unie90b': '回', 'unief70': '跟', 'uniec2a': '要', 'unif18e': '管', 'unif205': '打',
        'unie9ce': '最', 'unie4bd': '卓', 'unif471': '较', 'unie471': '近', 'unif583': '下', 'unie083': '头', 'unieacc': '喝',
        'unif671': '茶', 'unie01c': '再', 'uniebee': '微', 'uniea96': '笑', 'uniea41': '东', 'unif7c1': '西', 'unif0ff': '情',
        'unif8ae': '心', 'unie0e5': '性', 'unied48': '角', 'uniecd1': '手', 'uniece3': '而', 'unie568': '两', 'unif826': '天',
        'unif133': '向', 'unie545': '作', 'unie888': '局', 'unie6ef': '觉', 'unieebc': '停', 'unie930': '银', 'unif4a4': '刚',
        'unif2a0': '给', 'uniec67': '道', 'unie0ec': '做', 'unie643': '感', 'unif1bf': '信', 'unief81': '造', 'unie92d': '美',
        'unie70e': '境'}
    print(''.join(font_to_value[i] if 'uni' in i else i for i in
                  re.findall(r'<e.*?>(.*?)</e>', info)))


get_need_k()

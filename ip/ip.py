import re

with open(r'ip.html', 'r+', encoding='utf-8') as f:
    html = f.read()
res = re.search('<body>(.*?)<body>', html, re.S).group(1)
res = re.sub(
    r'(<.*? class="KPNP">.*?</.*?>)|(<.*? class="TXYK">.*?</.*?>)|(<.*? style="display:none">.*?</.*?>)',
    '', res.split('<br>', 1)[-1])
res = re.sub(
    r'<.*?>(.*?)</.*?>',
    r'\1', res)
res = res.replace('\n', '').split('<br>')
print(res, len(res))

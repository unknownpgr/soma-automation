import csv
import json
from requests.models import ContentDecodingError
import soma

s = soma.login(*json.load(open('secrets.json')))

# 글을 하나 작성한 후 개발자 도구에서 쿼리를 확인, 이 부분을 업데이트하세요.
payload = {
    'pageQueryString': 'menuNo=200053&pageIndex=1',
    'foundId': '1036',
    'csrfToken': '',
    'menuNo': '200053',
    'classId': '12',
    'atchFileId': '',
    'foundTyCd': 'eduFee',
    'reqSj': '자기주도학습비',
    'edufeeId_1': '1584',
    'regItem_1': '1',
}

for row in csv.reader(open('book.csv', 'r')):
    # 연번,항목,링크,가격,시간,목적,
    print(row)
    num, name, link, price, time, purpose, form, _ = row
    # payload[f'addItem_{num}'] = num
    payload[f'eduNm_{num}'] = name
    payload[f'eduPurpose_{num}'] = purpose
    payload[f'schedule_{num}'] = '무제한'
    payload[f'eduForm_{num}'] = form
    payload[f'onlineSite_{num}'] = link
    payload[f'eduTime_{num}'] = time
    payload[f'eduFee_{num}'] = price

res = s.post(
    'https://www.swmaestro.org/sw/mypage/eduFee/update.do', data=payload)
print(res.text)

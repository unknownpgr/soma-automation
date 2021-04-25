import json
import bs4
from requests.models import ContentDecodingError
import soma

s = soma.login(*json.load(open('secrets.json')))

lectures = []

for i in range(1, 100):
    res = s.get(
        f'https://www.swmaestro.org/sw/mypage/mentoLec/list.do?menuNo=200046&pageIndex={i}')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    table = soup.find('tbody')
    contents = table.find_all('tr')
    print('page :', i)
    if len(contents) == 0 or '데이터가 없습니다.' in table.text:
        print("No more data from page ", i)
        break
    for row in contents:
        items = row.find_all('td')
        if len(items) < 5:
            continue
        aTag = items[1].find('a')
        data = {
            'title': aTag.text.strip(),
            'link': f'https://www.swmaestro.org{aTag["href"]}',
            'date': items[3].text.strip(),
            'available': items[5].text.strip(),
            'mentor': items[6].text.strip()
        }
        lectures.append(data)

with open('lecture-all.json', 'w') as f:
    json.dump(lectures, f)

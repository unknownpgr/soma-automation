import json
import bs4
from requests.models import ContentDecodingError
import soma

s = soma.login(*json.load(open('secrets.json')))

lectures = []

for i in range(1, 100):
    res = s.get(
        f'https://www.swmaestro.org/sw/mypage/userAnswer/history.do?menuNo=200047&pageIndex={i}')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    table = soup.find('tbody')
    contents = table.find_all('tr')
    if len(contents) == 0:
        print("No more data from page ", i)
        break
    for row in contents:
        items = row.find_all('td')
        if len(items) < 3:
            print(len(items))
            continue
        title = items[1].text.strip()
        registered = items[3].text.strip()
        print(f'[{registered}]  {title}')
        lectures.append({'title': title, 'registered': registered})

with open('lecture-mine.json', 'w') as f:
    json.dump(lectures, f)

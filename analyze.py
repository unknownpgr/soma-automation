import json
from datetime import datetime

lecture_mine = json.load(open('lecture-mine.json'))
lecture_mine = list(
    filter(lambda lecture: '완료' in lecture['registered'], lecture_mine))

lecture_all = json.load(open('lecture-all.json'))


def find_lecture(title):
    for lecture in lecture_all:
        if lecture['title'] == title:
            return lecture
    for lecture in lecture_all:
        if title in lecture['title']:
            return lecture
        if lecture['title'] in title:
            return lecture
    print("Unmatched lecture! :", title)
    return None


lecture_mine_full = list(
    map(lambda lecture: find_lecture(lecture['title']), lecture_mine))
lecture_mine_full.sort(key=lambda x: x['date'])

date_today = datetime.today()
print('Today :', date_today.strftime("%Y-%m-%d"))
print()

for lecture in lecture_mine_full:
    date_lecture = datetime.strptime(lecture["date"], '%Y-%m-%d')
    if date_lecture < date_today:
        continue

    print(f'[{lecture["date"]}][{lecture["mentor"]}]\t{lecture["title"]}')
    print(lecture['link'])
    print()

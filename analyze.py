import json

lecture_mine = json.load(open('lecture-mine.json'))
lecture_mine = list(
    filter(lambda lecture: '완료' in lecture['registered'], lecture_mine))

lecture_all = json.load(open('lecture-all.json'))


def find_lecture(title):
    for lecture in lecture_all:
        if lecture['title'] == title:
            return lecture
    return None


lecture_mine_full = list(
    map(lambda lecture: find_lecture(lecture['title']), lecture_mine))

lecture_mine_full.sort(key=lambda x: x['date'])

for lecture in lecture_mine_full:
    print(f'[{lecture["date"]}] {lecture["title"]}')

import requests
import bs4


def get_input_value(text, names):
    soup = bs4.BeautifulSoup(text, "html.parser")
    inputs = soup.find_all('input')
    ret = []
    for name in names:
        for input in inputs:
            if input['name'] == name:
                ret.append(input['value'])
                break
        else:
            ret.append(None)
    return ret


def login(username, password):
    s = requests.Session()
    res = s.get(
        'https://www.swmaestro.org/sw/member/user/forLogin.do?menuNo=200025')
    csrf_token = get_input_value(res.text, ['csrfToken'])[0]
    print('Get csrfToken :', csrf_token)

    res = s.post(url='https://www.swmaestro.org/sw/member/user/toLogin.do', data={
        'loginFlag': None,
        'menuNo': '200025',
        'csrfToken': csrf_token,
        'username': username,
        'password': password,
    })
    password, username = get_input_value(res.text, ['password', 'username'])
    print('Get userName :', username)
    print('Get password :', password)

    s.post('https://www.swmaestro.org/sw/login.do', data={
        'password': password,
        'username': username
    })

    return s

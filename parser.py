import requests
from bs4 import BeautifulSoup as bs

LOGIN_INFO = {
    'userId' : 'myidid',
    'userPassword' : 'mypassword123'
}

with requests.Session() as s:
    first_page = s.get('https://www.clien.net/service')
    html = first_page.text
    soup = bs(html, 'html.parser')
    csrf = soup.find('input', {'name': '_csrf'}) # input태그 중에서 name이 _csrf인 것을 찾습니다.
    print(csrf['value']) # 위에서 찾은 태그의 value를 가져옵니다.

    LOGIN_INFO = {**LOGIN_INFO, **{'_csrf' : csrf['value']}}
    print(LOGIN_INFO)
    
    login_req = s.post('https://www.clien.net/service/login', data=LOGIN_INFO)
    print(login_req.status_code)

    if login_req.status_code != 200:
        raise Exception('로그인 실패')

        post_one = s.get('https://clien.net/service/board/rule/10707408')
        soup = bs(post_one.text, 'html.parser')

        title = soup.select('#div_content > div.post-title > div.title-subject > div')
        contents = soup.select('#div_content > div.post.box > div.post-content > div.post-article.fr-view')
        print(title[0].text)
        print(contents[0].text)


# Webcrawling
# Daum News 목록 여러건의 기사와 본문 수지

import requests
from bs4 import BeautifulSoup

url = 'https://news.daum.net/ranking/popular/all'
result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')
url_list = doc.select('ul.list_news2 a.link_txt')
for i, url in enumerate(url_list):
    print(f'## NEWS {i+1}번#######################')
    new_url = url['href']
    print(f'# URL: {new_url}')

    result = requests.get(new_url)

    # <tag id or class> </tag>
    # class => .
    # id => #

    doc = BeautifulSoup(result.text, 'html.parser')
    title = doc.select('h3.tit_view')[0].get_text()
    contents = doc.select('div p')
    contents.pop(-1)  # 마지막 정보 삭제
    content = ''  # 본문 총합
    for info in contents:
        content += info.get_text()


    print(' 뉴스 제목: {}'.format(title))
    print(f'뉴스 본문: {content}')
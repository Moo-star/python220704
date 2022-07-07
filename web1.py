# web1.py
# 웹 크롤링(웹 데이터 수집 기술)
from bs4 import BeautifulSoup

# 문서 로딩(메서드 체인)
page = open("c:\\work\\test01.html", "rt", encoding='utf-8').read()
# 검색이 용이한 객체(html, xml)
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())

#print(soup.prettify())
# 문서의 <p> 모두 검색(list)
#print(soup.find_all("p"))
#print(soup.find_all("a"))
#첫번째 <p> 검색
#print(soup.find("p"))

#<p class=outer-text>: 약간의 검색 조건
#print(soup.find_all("p", class_="outer-text"))

#문자열만 추출(웻봇 - 웻로봇)
for item in soup.find_all("p"):
    # 내부를 삭제하고 내부 컨텐츠만 리턴
    title = item.text
    title = title.replace("\n", "")
    title = title.replace("\t","")
    print(title.strip())




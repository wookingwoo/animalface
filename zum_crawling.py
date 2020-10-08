from bs4 import BeautifulSoup
from urllib.request import urlopen

print("줌 실시간 검색어 크롤링을 시작합니다.")


response = urlopen('https://zum.com')
soup = BeautifulSoup(response, 'html.parser')
i = 1
f = open("data/zum_trendingTopics.txt", 'w')
for anchor in soup.select("span.keyword.d_keyword"):
    data = str(i) + "위 : " + anchor.get_text() + "\n"
    i = i + 1
    f.write(data)
    print(data)
print("줌 실시간 검색어 크롤링을 마쳤습니다.")

f.close()
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://vibe.naver.com/chart/total')
soup = BeautifulSoup(response, 'html.parser')
print(soup.a)
print(soup.find_all("a"))

i = 1
f = open("새파일.txt", 'w')
for anchor in soup.find_all("div"):
    
    print(anchor)
    
    data = str(i) + "위 : " + anchor.get_text() + "\n"
    i = i + 1
    f.write(data)
f.close()
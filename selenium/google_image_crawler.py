from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome('./ChromeDriver/chromedriver_win32/chromedriver.exe')
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("wookingwoo")  # 구글 이미지 검색창에 내용 입력
elem.send_keys(Keys.RETURN)  # 엔터 입력

SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")  # 스크롤 높이 구해서 저장
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 스크롤을 내림
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")  # 스크롤 높이
    if new_height == last_height:  # 이전스크롤 높이와 현재 스크롤 높이가 같으면 (스크롤이 끝가지 다 내려가면, 더이상 스크롤이 안되면)
        try:
            driver.find_element_by_css_selector(".mye4qd").click()  # 구글에서 이미지 더보기 클릭
        except:
            break  # 이미지더보기 버튼이 없는경우 무한루프 탈출
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")  # 썸네일 이미지
count = 1
for image in images:
    try:
        image.click()  # 썸네일 이미지 클릭
        time.sleep(2)  # 이미지 로딩할때까지 2초 쉼
        imgUrl = driver.find_element_by_xpath(
            '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute(
            "src") # 큰 이미지

        # 봇으로 인식해 차단하는경우를 막기위해 header 추가
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, "./crawling_data/" + str(count) + ".jpg") # 이미지 저장
        count = count + 1
    except:
        pass

driver.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
import math

start_time = time.time()

people_list = ["방탄소년단 정국", "아이콘 바비", "워너원 박지훈", "엑소 수호",
               "한지민", "박보영", "윤승아", "한가인",
               "유인영", "차예련", "경리", "안소희",
               "이연희", "설현", "윤아", "고아라",
               "수지", "성유리", "트와이스 나연", "트와이스 다현",
               ]

if not os.path.exists('./crawling_data/'):
    os.makedirs('./crawling_data/')

for people_index in range(len(people_list)):

    driver = webdriver.Chrome('./ChromeDriver/chromedriver_win32/chromedriver.exe')
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")

    print(people_list[people_index], "크롤링을 시작합니다.")
    print("현재 실행 시간: %s seconds" % (time.time() - start_time))
    print("진행 현황:", round(((people_index + 1)/len(people_list))*100, 2) ,"(", people_index + 1, "/", len(people_list), ")")

    people_img_path = './crawling_data/' + people_list[people_index]

    if not os.path.exists(people_img_path):
        os.makedirs(people_img_path)
        print(people_list[people_index], "폴더가 없어 새로 생성하였습니다.")

    elem.send_keys(people_list[people_index])  # 구글 이미지 검색창에 내용 입력
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
                "src")  # 큰 이미지

            # 봇으로 인식해 차단하는경우를 막기위해 header 추가
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent',
                                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, people_img_path + "/" + str(count) + ".jpg")  # 이미지 저장
            count = count + 1

            if count == 51:
                break
        except:
            pass  # 크롤링중 오류난 사진은 패스

    driver.close()

print("크롤링을 성공적으로 모두 마치고 종료합니다.")
print("크롤링 이미지 수:", count)
print("최종 크롤링 시간: %s seconds" % (time.time() - start_time))

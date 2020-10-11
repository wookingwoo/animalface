from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
import datetime
import winsound


def mel_sound():  # 도,레,미,파,솔,라,시 Hz
    so1 = {'do': 261, 're': 293, 'mi': 329, 'pa': 349, 'sol': 391, 'ra': 440, 'si': 493, 'do5': 523, 'D5': 587}

    mel = ['do', 'mi', 'sol', ]
    dur = [3, 3, 3, ]

    mel2 = ['sol', ]
    dur2 = [2]

    mel3 = ['D5', 'D5', 'D5', 'D5', 'D5', ]
    dur3 = [4, 4, 4, 4, 4, ]

    music_domisol = zip(mel, dur)
    music_sol = zip(mel2, dur2)
    music_re5 = zip(mel3, dur3)

    for melody, duration in music_domisol:
        winsound.Beep(so1[melody], 1000 // duration)

    for melody, duration in music_sol:
        winsound.Beep(so1[melody], 1000 // duration)

    for melody, duration in music_re5:
        winsound.Beep(so1[melody], 1000 // duration)


mel_sound()

start_time = time.time()

people_list = ["강아지상 여자 연예인",
               "고양이상 여자 연예인",
               "사슴상 여자 연예인",
               "토끼상 여자 연예인",
               "강아지상 남자 연예인",
               "고양이상 남자 연예인",
               "곰상 남자 연예인",
               "공룡상 남자 연예인",
               "토끼상 남자 연예인",
               ]

if not os.path.exists('./crawling_data/'):
    os.makedirs('./crawling_data/')
    print('./crawling_data/' + "폴더가 없어 새로 생성하였습니다.")

now = datetime.datetime.now()
nowDatetime = now.strftime('%Y.%m.%d_%Hh%Mm%Ss')  # 2020.10.11_14h00m53s

if not os.path.exists('./crawling_data/' + nowDatetime):
    os.makedirs('./crawling_data/' + nowDatetime)
    print('./crawling_data/' + nowDatetime + "폴더가 없어 새로 생성하였습니다.")

for people_index in range(len(people_list)):

    start_person_time = time.time()

    driver = webdriver.Chrome('./ChromeDriver/chromedriver_win32/chromedriver.exe')
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")

    print(people_list[people_index], "크롤링을 시작합니다.")
    print("현재 실행 시간: %s seconds" % round((time.time() - start_time), 2))
    print("진행 현황:", round(((people_index + 1) / len(people_list)) * 100, 2), "%", "(", people_index + 1, "명 /",
          len(people_list), "명 )")

    people_img_path = './crawling_data/' + nowDatetime + "/" + people_list[people_index]

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
    print(people_list[people_index], "다운 현황:", end=" ")
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
            print(count, end=", ")

            count = count + 1

            # if count ==51:
            #     break
        except:
            pass  # 크롤링중 오류난 사진은 패스
    print("/", end=" ")

    driver.close()
    print("%s seconds" % round((time.time() - start_person_time), 2))

print("크롤링을 성공적으로 모두 마치고 종료합니다.")
print("크롤링 이미지 수:", count)
print("최종 크롤링 시간: %s seconds" % (time.time() - start_time))

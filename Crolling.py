from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pymysql
import warnings # 경고창 무시
import time
warnings.filterwarnings('ignore')

conn = pymysql.connect(
	                    user    = '',
                        passwd  = '',
    	                port    = 0000,
						db      = 'Music',
    	                charset = 'utf8'
)

cur = conn.cursor()

# url = "https://www.melon.com/"

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(3)
# driver.maximize_window()

# driver.get(url)
# driver.implicitly_wait(5)

# # 멜론 DJ 클릭
# driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[4]/a/span[2]').click()
# driver.implicitly_wait(5)

# # #테마장르 클릭
# driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[1]/li[4]/div/ul/li[3]/a/span').click()
# driver.implicitly_wait(5)
# thema_url = driver.current_url
# # 테마를 차례대로 클릭
# for i in [5, 7, 14]:
#     driver.find_element_by_xpath(f'//*[@id="tab1"]/li[{i}]/a').click()
#     playlist_url = driver.current_url
#     driver.implicitly_wait(5)
#     num = int(input("가지고 오고싶은 플레이리스트 수 : "))
#     # 첫번째 곡 부터 클릭후 노래 정보 가져오기 
#     for j in range(1, num+1):
#         driver.find_element_by_xpath(f'//*[@id="djPlylstList"]/div/ul/li[{j}]/div[2]/div[1]/a[2]').click()
#         driver.implicitly_wait(5)
#         time.sleep(3)
#         driver.find_element_by_xpath(f'//*[@id="pageObjNavgation"]/div/span/a[{x}]').click()
        # url = driver.current_url
        # driver.get(url)
        # driver.implicitly_wait(5)
        # time.sleep(3)
        # for z in range(1, len(driver.find_elements_by_tag_name("tr"))):
        #     driver.find_element_by_xpath(f'//*[@id="frm"]/div/table/tbody/tr[{z}]/td[4]/div/a').click()
        #     driver.implicitly_wait(5)
        #     artist_name = driver.find_element_by_class_name("artist_name").text                
        #     song_name = driver.find_element_by_class_name("song_name").text
        #     lyric = driver.find_element_by_class_name("lyric").text
        #     music = (artist_name, song_name, lyric)
        #     cur.execute('INSERT IGNORE INTO music (artist_name, song_name, lyrics) VALUES (%s ,%s, %s)', music)
        #     conn.commit()
        #     driver.back()
        #     driver.implicitly_wait(5)
#         if int(driver.find_element_by_class_name("sum").text[1:-1]) % 50 != 0:
#             page = int(driver.find_element_by_class_name("sum").text[1:-1]) // 50 + 1
#         else:
#             page = int(driver.find_element_by_class_name("sum").text[1:-1]) // 50
#         for x in range(1, page):
#             driver.find_element_by_xpath(f'//*[@id="pageObjNavgation"]/div/span/a[{x}]').click()
#             url = driver.current_url
#             driver.get(url)
#             driver.implicitly_wait(5)
#             time.sleep(3)
#             for y in range(1, len(driver.find_elements_by_tag_name("tr"))):
#                 driver.find_element_by_xpath(f'//*[@id="frm"]/div/table/tbody/tr[{y}]/td[4]/div/a').click()
#                 driver.implicitly_wait(5)
#                 artist_name = driver.find_element_by_class_name("artist_name").text                
#                 song_name = driver.find_element_by_class_name("song_name").text
#                 lyric = driver.find_element_by_class_name("lyric").text
#                 music = (artist_name, song_name, lyric)
#                 cur.execute('INSERT IGNORE INTO music (artist_name, song_name, lyrics) VALUES (%s ,%s, %s)', music)
#                 conn.commit()
#                 driver.back()
#                 driver.implicitly_wait(5)
#                 time.sleep(3)
#         driver.get(playlist_url)
#     driver.get(thema_url)

# driver.quit()






driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.maximize_window()


page = int(input("수집할 곡 수를 입력해주세요 : "))
time.sleep(3)
for i in range(551, page, 50):
    url = f'https://www.melon.com/genre/song_list.htm?gnrCode=GN0100#params%5BgnrCode%5D=GN0100&params%5BdtlGnrCode%5D=&params%5BorderBy%5D=POP&params%5BsteadyYn%5D=N&po=pageObj&startIndex={i}'
    driver.get(url)
    driver.implicitly_wait(5)
    driver
    time.sleep(3)
    for x in range(1, len(driver.find_elements_by_tag_name("tr"))):
        driver.find_element_by_xpath(f'//*[@id="frm"]/div/table/tbody/tr[{x}]/td[4]/div/a').click()
        driver.implicitly_wait(5)
        time.sleep(3)
        if len(driver.find_element_by_class_name('wrap_lyric').text) <= 60:
            driver.back()
            continue
        artist_name = driver.find_element_by_class_name("artist_name").text                
        song_name = driver.find_element_by_class_name("song_name").text
        lyric = driver.find_element_by_class_name("lyric").text
        music = (artist_name, song_name, lyric)
        cur.execute('INSERT IGNORE INTO music (artist_name, song_name, lyrics) VALUES (%s ,%s, %s)', music)
        conn.commit()
        driver.back()
        driver.implicitly_wait(5)
        time.sleep(3)


driver.quit()

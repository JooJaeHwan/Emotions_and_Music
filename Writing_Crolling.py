from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
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

url = "https://teen.munjang.or.kr/archives/category/old-excl"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.maximize_window()

driver.get(url)
driver.implicitly_wait(30)
st = []
for i in range(1, 41):
    url = f'https://teen.munjang.or.kr/archives/category/old-excl/page/{i}'
    driver.implicitly_wait(30)
    driver.get(url)

    html = driver.page_source 
    soup = BeautifulSoup(html, 'html.parser')
    temp = [i['id'] for i in soup.select('#main > article[id]')]
    for t in temp:
        if [i.text for i in soup.select(f'#{t} > div > div.post_content > div.post_title > p')] == []:
            driver.find_element_by_xpath(f'//*[@id="{t}"]/div/div[2]/div[1]/a').click()
            driver.implicitly_wait(30)
            time.sleep(5)
            for s in driver.find_element_by_class_name("entry-content").text.split("\n"):
                if len(s) <= 10:
                    continue
                cur.execute('INSERT IGNORE INTO writing (sentences) VALUES (%s)', s)
                conn.commit()
        else: continue
 
        driver.back()
    print(f'{i}페이지 끝')
    

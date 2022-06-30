from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pymysql
import warnings # 경고창 무시
import time
import re
warnings.filterwarnings('ignore')


conn = pymysql.connect(
	                    user    = '',
                        passwd  = '',
    	                port    = 0000,
						db      = 'Writing',
    	                charset = 'utf8'
)

cur = conn.cursor()


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.maximize_window()
driver.implicitly_wait(3)
st = []
for i in range(1, 41):
    url = f'https://teen.munjang.or.kr/archives/category/write/life/page/{i}'
    driver.implicitly_wait(3)
    driver.get(url)

    html = driver.page_source 
    soup = BeautifulSoup(html, 'html.parser')
    temp = [i['id'] for i in soup.select('#main > article[id]')]
    for t in temp:
        if "추천해요" in [i.text for i in soup.select(f'#{t} > div > div.post_content > div.post_title > a')][0]:
            continue
        if [i.text for i in soup.select(f'#{t} > div > div.post_content > div.post_title > p')] == [] and [i.text for i in soup.select(f'#{t} > div > div.post_content > div.post_title > a > span')] != ['[공지] ']:
            driver.find_element_by_xpath(f'//*[@id="{t}"]/div/div[2]/div[1]/a').click()
            driver.implicitly_wait(30)
            sentence = driver.find_element_by_class_name("entry-content").text.split("\n")
            time.sleep(5)
            for s in sentence:
                s = s.strip()
                s = re.sub(r'[^가-힣A-Za-z0-9\.\,\!\?\s]', '', s)
                s = re.sub('  +', " ", s)
                if len(s) <= 25:
                    continue
                cur.execute('INSERT IGNORE INTO essay (sentences) VALUES (%s)', s)
                conn.commit()
        else: continue
 
        driver.back()
    print(f'{i}페이지 끝')
driver.quit()    

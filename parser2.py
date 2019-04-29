from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/태형/Desktop/crawling/chromedriver') 
#driver = webdriver.PhantomJS('C:/Users/태형/Desktop/crawling/phantomjs-2.1.1-windows/bin/phantomjs')
driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login')

driver.find_element_by_name('id').send_keys('ussu1112')
driver.find_element_by_name('pw').send_keys('qkfrdmsekfk12!')

driver.find_element_by_xpath(
    '//*[@id="frmNIDLogin"]/fieldset/input'
    ).click()

driver.get('https://comic.naver.com/index.nhn')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser2')
notices = soup.select('#content > div.list_area.daily_all > div:nth-child(1) > div > ul')

for n in notices :
    print(n.text.strip())
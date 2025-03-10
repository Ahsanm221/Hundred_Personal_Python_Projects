from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Users/ahsanmustafa/Selenium Development/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
# print(article_count)
# article_count.click()

all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Keys.")
search.send_keys(Keys.ENTER)


time.sleep(15)

driver.close()

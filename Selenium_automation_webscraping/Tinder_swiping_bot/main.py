from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

USERNAME = "gorbapyo444@gmail.com"
PASSWORD = "#Qwer4321"

chrome_options = Options()
driver_path = "/Users/ahsanmustafa/Selenium Development/chromedriver"

service = Service(driver_path)
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.tinder.com")
sleep(2)
login_button = driver.find_element(By.XPATH, "//*[@id='s571767047']/div/div[1]/div/main/div["
                                             "1]/div/div/div/div/header/div/div[2]/div[2]/a")
login_button.click()

sleep(2)
login_fb_button = driver.find_element(By.XPATH, "//*[@id='s-1156614029']/main/div/div/div[1]/div/div/div[2]/div["
                                                "2]/span/div[2]/button")
login_fb_button.click()
sleep(3)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)


sleep(2)

email_input = driver.find_element(By.ID, "email")
email_input.send_keys(USERNAME)
password_input = driver.find_element(By.ID, "pass")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

# fill in the facebook login details
# NoSuchElementException - add delay b/w clicks

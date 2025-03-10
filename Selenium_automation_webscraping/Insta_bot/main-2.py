from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time
from selenium.webdriver.chrome.service import Service


CHROME_DRIVER_PATH = "/Users/ahsanmustafa/Selenium Development/chromedriver"
SIMILAR_ACCOUNT = "gordongram"
USERNAME = "gorbapyo444@gmail.com"
PASSWORD = "#Qwer4321"

service = Service(CHROME_DRIVER_PATH)


class InstaFollower:

    def __init__(self, service_):
        self.driver = webdriver.Chrome(service=service_)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(15)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(20)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(20)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(8)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(8)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(service)
bot.login()
bot.find_followers()
bot.follow()

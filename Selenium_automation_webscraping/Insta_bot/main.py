from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

EMAIL = "gorbapyo444@gmail.com"
PASSWORD = "#Qwer4321"
USERNAME = "gorbaterapyo"
SIMILAR_ACC = "gordongram"

driver_path = "/Users/ahsanmustafa/Selenium Development/chromedriver"

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
service = Service(driver_path)


class InstaFollower:
    def __init__(self, service_):
        self.driver = webdriver.Chrome(service=service_)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(20)
        email_input = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input")
        email_input.send_keys(EMAIL)
        password_input = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(50)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACC}/")
        sleep(40)
        followers = self.driver.find_element(By.CSS_SELECTOR, '#mount_0_0_1N > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z > div.x9f619.xnz67gz.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.xh8yej3.x1gryazu.x10o80wk.x14k21rp.x1porb0y.x17snn68.x6osk4m > div:nth-child(2) > section > main > div > header > section > ul > li:nth-child(2) > a')
        followers.click()

    def follow(self):
        try:
            follow_button = self.driver.find_elements(By.CSS_SELECTOR, "button")
            for follower in follow_button:
                print(follower.text)
                if follower.text == "Follow":
                    print("click")
                    follower.click()
                    sleep(8)
        except Exception as e:
            print(e)


instabot = InstaFollower(service)
instabot.login()
instabot.find_followers()
instabot.follow()

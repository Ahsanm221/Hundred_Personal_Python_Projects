from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

EMAIL = "gorbaterapyo@gmail.com"
PASSWORD = "#Qwer4321"
USERNAME = "gorbaterapyo"

PROMISED_DOWN = 20
PROMISED_UP = 15
driver_path = "/Users/ahsanmustafa/Selenium Development/chromedriver"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(driver_path)


class InternetSpeedTwitterBot:
    def __init__(self, service_, chrome_options_):
        self.up = 0
        self.down = 0
        self.driver = webdriver.Chrome(service=service_, options=chrome_options_)

    def get_internet_speed(self):
        pass
        # self.driver.get("https://www.speedtest.net/")
        # go_button = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div["
        #                                                "3]/div[1]/a/span[4]")
        # go_button.click()
        # sleep(60)
        # self.down = float(self.driver.find_element(By.CSS_SELECTOR, "div .download-speed").text)
        # self.up = float(self.driver.find_element(By.CSS_SELECTOR, "div .upload-speed").text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(30)
        email_input = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div['
                                                         '2]/div[2]/div/div/div[2]/div[2]/div/div/div/div['
                                                         '5]/label/div/div[2]/div/input')
        email_input.send_keys(EMAIL)
        email_input.send_keys(Keys.ENTER)
        sleep(2)
        # unusual activity, so add username to next pop-up before pass
        username_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                            '2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                            '2]/label/div/div[2]/div/input')
        username_input.send_keys(USERNAME)
        username_input.send_keys(Keys.ENTER)
        sleep(2)
        pass_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                        '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                        '3]/div/label/div/div[2]/div[1]/input')
        pass_input.send_keys(PASSWORD)
        pass_input.send_keys(Keys.ENTER)
        sleep(10)

        txt_box = self.driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > '
                                                            'div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > '
                                                            'div > div > div > div > div > '
                                                            'div.css-1dbjc4n.r-kemksi.r-184en5c > div > '
                                                            'div.css-1dbjc4n.r-kemksi.r-oyd9sg > div:nth-child(1) > '
                                                            'div > div > div > '
                                                            'div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a'
                                                            '.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > '
                                                            'div.css-1dbjc4n.r-184en5c > div > div > div > div > div '
                                                            '> div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q '
                                                            '> div > div > div > div > label > '
                                                            'div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > '
                                                            'div > div > div.DraftEditor-editorContainer > div > div '
                                                            '> div > div')
        txt_box.click()
        tweet = f"Hey internet provider, why is my internet speed {self.down}down/{self.up}up when I pay for " \
                f"{PROMISED_DOWN}down/{PROMISED_UP}up?"
        txt_box.send_keys(tweet)
        sleep(3)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                          '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                          '1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        tweet_button.click()

        sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(service, chrome_options)
bot.get_internet_speed()
bot.tweet_at_provider()

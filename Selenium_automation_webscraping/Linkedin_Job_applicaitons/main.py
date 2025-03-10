from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# USERNAME = "gorbapyo444@gmail.com"
# PASSWORD = "#Qwer4321"

driver_path = "/Users/ahsanmustafa/Selenium Development/chromedriver"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(3)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(USERNAME)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)
time.sleep(3)
save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
# save_button = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div["
#                                             "1]/div[4]/div/button")
save_button.click()

time.sleep(5)


driver.close()

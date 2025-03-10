from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/ahsanmustafa/Selenium Development/chromedriver"
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)

# -------------------------------- FINDING PRICE OF A SHOE AT AMAZON -------------------------------- #
# driver.get("https://www.amazon.com/Nike-Retro-DD1399-Black-White/dp/B0B1VXQ1KX/ref=sr_1_31?keywords=nike%2Bsneakers"
#            "%2Bmen&qid=1685531414&sprefix=nike%2Bsnea%2Caps%2C473&sr=8-31&th=1")
# # price = driver.find_element(By.CLASS_NAME, "a-price-range")
#
# price = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[1]/span[2]')
# print(price.text)
# -------------------------------- UPCOMING EVENTS AT PYTHON.ORG -------------------------------- #

driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# events = {}
#
# for n in range(0, len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text,
#     }

# -------------------------------------------------------- #
# events = {new_key:new_value for item in list}
# events = {new_key:new_value for (key, value) in dictionary.items()}
# -------------------------------------------------------- #

events = {n: {"time": event_times[n].text,"name": event_names[n].text} for n in range(0, len(event_times))}
print(events)

driver.quit()

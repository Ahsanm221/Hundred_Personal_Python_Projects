from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "/Users/ahsanmustafa/Selenium Development/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

money = driver.find_elements(By.CSS_SELECTOR, "#rightPanel #store b")
# Get all upgrade <b> tags
store_items = [item.text for item in money]
store_items.remove("")

item_ids = [item.split("-")[0].strip() for item in store_items]
# Convert <b> text into an integer price.
item_prices = [int(item.split("-")[1].strip().replace(",", "")) for item in store_items]

cookie = driver.find_element(By.CSS_SELECTOR, "#middle #cookie")
# Create dictionary of store items and prices
cookie_upgrades = {item_prices[n]: item_ids[n] for n in range(0, len(item_ids))}
print(cookie_upgrades)

timeout = time.time() + 5
five_min = time.time() + 300
one_min = time.time() + 60

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:
        # Get current cookie count
        current_money = driver.find_element(By.CSS_SELECTOR, "#money").text
        if "," in current_money:
            current_money = current_money.replace(",", "")
        cookie_count = int(current_money)

        # Find upgrades that we can currently afford
        affordable_upgrades = {cost: id_ for (cost, id_) in cookie_upgrades.items() if cookie_count > cost}

        # Purchase the most expensive affordable upgrade
        if time.time() > one_min:
            cookie_upgrades.pop(100, None)
            affordable_upgrades.pop(100, None)

        if len(affordable_upgrades) == 0:
            pass
        else:
            highest_affordable_upgrade_price = max(affordable_upgrades)
            to_purchase_id = affordable_upgrades[highest_affordable_upgrade_price]

            driver.find_element(By.ID, "buy"+to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break


driver.close()

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

driver_path = "/Users/ahsanmustafa/Selenium Development/chromedriver"
service = Service(driver_path)

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSe56NmcdfqVlEerfgjj8ZJirOouF02n7THTzWpDSZMa-MYIDg/viewform?usp" \
           "=sf_link"
ZILLOW = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
         "%22mapBounds%22%3A%7B%22north%22%3A37.86289213928623%2C%22east%22%3A-122.30252353076172%2C%22south%22%3A37" \
         ".68758784905548%2C%22west%22%3A-122.56413546923828%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C" \
         "%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore" \
         "%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D" \
         "%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22" \
         "%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C" \
         "%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D" \
         "%5D%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/16.4 Safari/605.1.15",
    "Accept-Language": "en-GB,en;q=0.9",
}

response = requests.get(url=ZILLOW, headers=headers)

zillow_html = response.text
soup = BeautifulSoup(zillow_html, "html.parser")
apartment_links = []
apartment_addresses = []

apartments_info = soup.select("ul li a")

for each in apartments_info:
    link = each["href"]
    if link[:5] != "https":
        link = "https://www.zillow.com" + link
        apartment_links.append(link)
    else:
        apartment_links.append(link)
    address = each.find(name="address")
    try:
        apartment_addresses.append(address.getText())
    except AttributeError:
        continue

# price_info = soup.find_all('span', attrs={"data-test": "property-card-price"})
price_info = soup.select("ul li div div span")
apartment_prices = [each.text for each in price_info]

# addresses = soup.select("ul li a address")

# for each in apartments_info:
#     anchor = each.find(name="a")
#     link = anchor["href"]
#     if link[:5] != "https":
#         link = "https://www.zillow.com" + link
#         apartment_links.append(link)
#     else:
#         apartment_links.append(link)
#
#     address = (each.find(name="address").getText()).split(" | ")[-1]
#     apartment_addresses.append(address)
#     # srp__sc-16e8gqd-1 - jLQjry
#     price = (each.find(class_="srp__sc-16e8gqd-1 jLQjry", name="span").getText()).split("+")[0].strip("/mo")
#     apartment_prices.append(price)

# -------------- SELENIUM ---------- #
# driver = webdriver.Chrome(service=service)
# driver.get(FORM_URL)
# for n in range(0, len(apartment_links)):
#     address_field = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > "
#                                                          "div:nth-child(1) > div > div > div.AgroKb > div > "
#                                                          "div.aCsJod.oJeWuf > div > div.Xb9hP > input")
#     address_field.send_keys(apartment_addresses[n])
#
#     price_field = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > "
#                                                        "div:nth-child(2) > div > div > div.AgroKb > div > "
#                                                        "div.aCsJod.oJeWuf > div > div.Xb9hP > input")
#     price_field.send_keys(apartment_prices[n])
#
#     link_field = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child("
#                                                       "3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > "
#                                                       "div.Xb9hP > input")
#     link_field.send_keys(apartment_links[n])
#
#     submit_button = driver.find_element(By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > "
#                                                          "div.DE3NNc.CekdCb > div.lRwqcd > div > span > span")
#     submit_button.click()
#     sleep(3)
#
#     another_resp = driver.find_element(By.CSS_SELECTOR, "body > div.Uc2NEf > div:nth-child(2) > div.RH5hzf.RLS9Fe > "
#                                                         "div > div.c2gzEf > a")
#     another_resp.click()


print(apartment_links)
print(apartment_prices)
print(apartment_addresses)

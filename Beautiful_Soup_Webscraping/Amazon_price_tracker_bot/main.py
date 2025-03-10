import requests
from bs4 import BeautifulSoup
import smtplib

MY_IDEAL_PRICE = 150
MY_EMAIL = "gorbapyo444@gmail.com"
PASSWORD = "ddnmynrijonbbeel"
URL = "https://www.amazon.com/Nike-Retro-DD1399-Black-White/dp/B0B1VXQ1KX/ref=sr_1_31?keywords=nike%2Bsneakers%2Bmen" \
     "&qid=1685531414&sprefix=nike%2Bsnea%2Caps%2C473&sr=8-31&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/16.4 Safari/605.1.15",
    "Accept-Language": "en-GB,en;q=0.9",
}
response = requests.get(url=URL,
                        headers=headers)

amazon_html = response.text
soup = BeautifulSoup(amazon_html, "html.parser")

price = soup.find(class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_float = float(price_without_currency)
product_title = soup.find(id="productTitle").getText()


if price_float < MY_IDEAL_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="ahsanmustafa30@gmail.com",
                            msg=f"Subject:Amazon Price Alert!\n\n{product_title}\nis now: ${price_float}\n{URL}")

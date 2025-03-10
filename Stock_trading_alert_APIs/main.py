import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"



alpha_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=alpha_params)
response.raise_for_status()

data = response.json()

previous_days_data = data["Time Series (Daily)"]
data_list = [value for (key, value) in previous_days_data.items()]

yesterday_closing_price = data_list[0]["4. close"]
day_before_yesterday_closing_price = data_list[1]["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
percentage = round(difference / float(yesterday_closing_price) * 100)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if abs(percentage) > 1:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "to": "2023-05-19",
        "from": "2023-05-17"
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()["articles"][:3]
    print(news_data)
    formatted_article_list = [f"{STOCK_NAME}: {up_down}{percentage}%\nHeadline: {article['title']}."
                              f" \nBrief: {article['description']}" for article in news_data]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_article_list:
        message = client.messages.create(
            body=article,
            from_="+12545705891",
            to="+923365639812"
        )
else:
    print(percentage)

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
"""

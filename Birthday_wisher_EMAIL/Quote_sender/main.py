import smtplib
import datetime as dt
from random import choice

my_email = "gorbapyo444@gmail.com"
password = "ddnmynrijonbbeel"

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
date_of_birth = dt.datetime(year=2010, month=6, day=20)

if day_of_week == 3:
    with open("quotes.txt") as quote:
        list_quotes = quote.readlines()
        chosen_quote = choice(list_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="gorbaterapyo@gmail.com",
            msg=f"Subject:Hello\n\n{chosen_quote}")
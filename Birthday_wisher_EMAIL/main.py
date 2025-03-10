import pandas
import datetime as dt
from random import randint
import smtplib

# -------gmails------>>> gorbapyo444 | #Qwer4321 | gorbaterapyo
my_email = "gorbapyo444@gmail.com"
password = "ddnmynrijonbbeel"

today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if (today.month, today.day) in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    print(birthday_person)
    letter_number = randint(1, 3)
    with open(f"letter_templates/letter_{letter_number}.txt") as letter:
        letter_contents = letter.read()
        letter_contents = letter_contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{letter_contents}")

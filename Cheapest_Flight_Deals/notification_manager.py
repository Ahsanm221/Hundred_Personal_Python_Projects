from twilio.rest import Client
import smtplib




class NotificationManager:
    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )

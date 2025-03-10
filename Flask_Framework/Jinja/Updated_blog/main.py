from flask import Flask, render_template, request
import requests
import smtplib

blog_data_end_pt = 'https://api.npoint.io/2bdf0b90e530373dfbfb'
data = requests.get(blog_data_end_pt).json()

MY_EMAIL = "gorbapyo444@gmail.com"
PASSWORD = "ddnmynrijonbbeel"
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', all_posts=data)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route("/post/<int:id>")
def post(id):
    for each in data:
        if id == each["id"]:
            return render_template('post.html', post=each)


@app.route('/contact', methods=["POST", "GET"])
def receive_data():
    if request.method == "POST":
        data = request.form
        send_email(data['name'], data['email'], data['phone'], data['message'])
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName:{name}\nEmail:{email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)


if __name__ == '__main__':
    app.run(debug=True)

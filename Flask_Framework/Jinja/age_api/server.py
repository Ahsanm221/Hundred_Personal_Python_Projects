from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route("/guess/<name>")
def home(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = response.json()
    gen = gender_data["gender"]
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("index.html", name=name.title(), gender=gen, age=age)


@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

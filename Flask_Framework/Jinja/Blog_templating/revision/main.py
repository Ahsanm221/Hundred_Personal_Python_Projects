from flask import Flask, render_template
import requests

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:num>')
def show_post(num):
    # requested_post = None
    for post in posts:
        if num == post['id']:
            # requested_post = post
            return render_template("post.html", requested_post=post)


if __name__ == "__main__":
    app.run(debug=True)

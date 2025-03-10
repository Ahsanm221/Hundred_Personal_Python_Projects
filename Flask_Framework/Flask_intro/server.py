from flask import Flask
import random

app = Flask(__name__)
the_number = random.randint(0, 9)
print(the_number)


@app.route('/')
def higher_lower():
    return "<h1> Guess a number between 0 and 9 </h1>" \
           "<img src='https://media.giphy.com/media/BI63M9HL4PQyalOplZ/giphy.gif?cid=ecf05e4757ywl3ml9lkvrp6k688mg7kmiwjp8stb59l6ybpz&ep=v1_gifs_trending&rid=giphy.gif&ct=g'>"


@app.route('/<int:number>')
def numbers(number):
    if number > the_number:
        return '<h1 style="color: blue"> Too high! </h1>' \
               '<img src="https://media.giphy.com/media/W3QKEujo8vztC/giphy.gif?cid' \
               '=ecf05e47ki21amh8u7nbjiwggqprdre2nwsmnvrrl4ry3uin&ep=v1_gifs_trending&rid=giphy.gif&ct=g" >'
    elif number < the_number:
        return '<h1 style="color: purple"> Too low! </h1>' \
               '<img src="https://media.giphy.com/media/1k2LQ7vfnR7ghKWWb2/giphy.gif?cid' \
               '=ecf05e47ki21amh8u7nbjiwggqprdre2nwsmnvrrl4ry3uin&ep=v1_gifs_trending&rid=giphy.gif&ct=g" >'
    else:
        return '<h1 style="color: red"> You found me! </h1>' \
               '<img src="https://media.giphy.com/media/kxzeciyEDHdats8H7G/giphy.gif?cid' \
               '=ecf05e47ki21amh8u7nbjiwggqprdre2nwsmnvrrl4ry3uin&ep=v1_gifs_trending&rid=giphy.gif&ct=g">'


if __name__ == '__main__':
    app.run(debug=True)

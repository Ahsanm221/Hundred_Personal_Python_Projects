from flask import Flask


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def italic(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


app = Flask(__name__)


# @app.route('/')
# @italic
# @make_bold
# @underline
# def hello_world():
#     return '<h1 style="text-align: center">Hello world</h1>' \
#            '<p> This is a paragraph </p>'

#
# @app.route('/bye')
# @italic
# @make_bold
# @underline
# def bye():
#     return "Bye!"
#
#
# @app.route("/<name>/<number>")
# def greet(name, number):
#     return f"Hello there {name}! You are {number} years old."


# Advanced Python Decorator Functions
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("ahsan")
new_user.is_logged_in = True
create_blog_post(new_user)

# if __name__ == '__main__':
#     app.run(debug=True)

# def decorator_function(function):
#     def wrapper_function():
#         sleep(2)
#         function()
#         function()
#     return wrapper_function
#
#
# @decorator_function
# def hello():
#     print("Hello")
#
#
# hello()
#
#
# def bye():
#     print("Bye")
#
#
# bye_is_wrapped = decorator_function(bye)
# bye_is_wrapped()

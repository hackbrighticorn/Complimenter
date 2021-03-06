from flask import Flask, request, render_template
from random import choice, randint


app = Flask(__name__)


@app.route('/')
def index():
    return "<html><body><h1>I am the landing page</h1></body></html>"


@app.route('/hello')
def say_hello():
    return "<html><body><h1>Hello</h1></body></html>"


@app.route('/lucky')
def lucky_number():
    lucky_num = randint(1, 10)
    lucky_message = "Your lucky number is %s" % lucky_num
    return "<html><body><h1>" + lucky_message + "</h1></body></html>"


@app.route('/form')
def show_form():
    return render_template("form.html")

@app.route('/greet')
def offer_greeting():
    compliments = ["smart", "clever", "tenacious", "awesome", "Pythonic"]
    player = request.args.get("person")
    nice_thing = choice(compliments)
    return render_template("compliment.html", name = player, compliment = nice_thing)

if __name__ == "__main__":
    app.run(debug=True)
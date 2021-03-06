"""A simple Flask web application.

Lasya Sreepada
Yale University '19
CPSC 184

May 6, 2017
"""

from flask import Flask, render_template
import urllib.request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/reading")
def reading():
    return render_template('reading.html')

@app.route("/quiz")
def quiz():
    return render_template('quiz.html')

@app.route("/humor")
def humor():
    return render_template('humor.html')

@app.route("/memes")
def memes():
    return render_template('memes.html')

@app.route("/copyright")
def copyright():
    return render_template('copyright.html')

@app.route("/trademark")
def trademark():
    return render_template('trademark.html')

@app.route("/patent")
def patent():
    return render_template('patent.html')


if __name__ == "__main__":
    app.run()

if __name__ == "__quiz__":
    app.run()

if __name__ == "__memes__":
    app.run()

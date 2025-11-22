from flask import Flask, request
from random import randint, choice
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    phrases: list[str] = ['Welcome to this page!', 'Goose is a lovely boy dog!!', 'It\'s a wonderful day for a dog walk', 'You are looking great today!', 'Goose is looking beautful today!', 'The weather is excellent today!']
    return {'phrase': choice(phrases),
            'date': datetime.now()}



if __name__ == '__main__':
    app.run(debug=True, port=5020)
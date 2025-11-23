from flask import Flask, request
from random import randint, choice
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    phrases: list[str] = ['Welcome to this page!', 'Goose is a lovely boy dog!!', 'It\'s a wonderful day for a dog walk', 'You are looking great today!', 'Goose is looking beautful today!', 'The weather is excellent today!', 'You are looking wonderful today', 'What an excellent time for a walk with my favorite dog!!']
    return {'phrase': choice(phrases),
            'date': datetime.now()}


@app.route('/api/random') 
def random():
    number_input = request.args.get('number', type=int, default=100)
    text_input = request.args.get('text', type=str, default='default')

    if isinstance(number_input, int):
        return {
            'input': number_input,
            'random': randint(0, number_input),
            'text': text_input,
            'date': datetime.now()
        }
    else:
        return {'Error': 'Please only enter numbers.'}


if __name__ == '__main__':
    app.run(debug=True, port=5020)
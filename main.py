from flask import Flask
from random_word import RandomWords
r = RandomWords()
import os

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hey, we have Flask in a Docker container! %s' % (r.get_random_word())


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

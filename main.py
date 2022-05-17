from flask import Flask
from random_word import RandomWords
r = RandomWords()
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Random word! %s' % (r.get_random_word())

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)

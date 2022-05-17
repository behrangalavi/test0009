
from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return 'it works!'

from crypt import methods
from flask import Flask, render_template, request
import pandas as pd




app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html'), 200

@app.route('/info')
def info():

    return render_template('info.html'), 200

@app.route('/result', methods=["POST"])
def user():
    value_1 = request.form["name"]
    name = "%s"%value_1
    value_2 = request.form["situation"]
    situation = "%s"%value_2
    return render_template('result.html', name=name, situation=situation), 200


import os
import requests
import traceback
from flask import *

# from wtforms import Form, BooleanField, validators, SubmitField, StringField

app = Flask(__name__)
app.secret_key = b'\xa6\xdd\x99,\xd9F9\xcf\x12\xf6\xf7\x08tk\xd6\x7f\x02C\x8c&\xc7?*\x91'

@app.route('/',  methods = ['POST', 'GET'])

def home():
    return render_template('home.html')
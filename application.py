from flask import Flask 
import time
import datetime
import os

app = Flask(__name__)
DEBUG=('DEBUG' in os.environ and os.environ['DEBUG'] in ['1', 'true'])

@app.route('/')
def home():
    return '<h1>DevOps</h1>'
    
@app.route('/temperature=<x>')
def functionName(x):

    date = datetime.datetime.now()
    print(date)

    item = {
    "date" : date,
    "temperature" : x
    }

    return(item)

app.run(host = '0.0.0.0', port = 5551, debug=DEBUG)

#!flask/bin/python
from flask import Flask
import json

app = Flask(__name__)
response = "";
@app.route('/')
def index():
    outfile = open('data.txt', 'r')
    response = outfile.read()
    return response

if __name__ == '__main__':
    app.run(debug=True)



# This is the engine of the REST based flask API

from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
import pickle

from nltk.sem.evaluate import Error

app = Flask(__name__)  # intitialize the flaks app  # common 

import os
from flask import send_from_directory



@app.route('/', methods = ['POST', 'GET'])
def home():
    # do the pre processing on the text
    return render_template("index.html")
    

@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html'), 404

if __name__ == '__main__' :
    app.run(debug=True )  
    
    #,host="0.0.0.0")

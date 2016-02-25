from __future__ import print_function # In python 2.7
from flask import Flask
import os
import re
import sys

from os.path import expanduser
from flask import Flask, render_template, request
# home = expanduser("~")
# import imp
# imp.load_source('test', 'soa-test')

from test import *
from sheet import *



app = Flask(__name__)

@app.route("/")
def hello():
    create_file('naks')
    return '<form method="POST">XPLAN ID<input name="text"><input type="submit" value="submit"></form>'
 
@app.route("/", methods=['POST'])
def echo(): 

    aa = request.form['text']
    aa = aa.strip()
    # aa = int(aa)
    # return 'Nako'
    # if re.search(',', aa): # or (re.search(';', aa)):
    #     aa = aa.split(';')
    os.system('./client_partner_detailsV2.py "' + aa + '"')
    # return 'hello'
    # dump(aa)
    aa = os.popen('cat naks').read()
    return aa

if __name__ == "__main__":
    while True:
        app.run(debug=True)
    # hello()


# sudo kill `ps -fA | grep python |awk '{print $2}'`

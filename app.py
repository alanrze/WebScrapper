from flask import Flask, redirect, url_for, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/success/<name>')
def success(name):
   finJ={}
   import bestbuyServer
   import WalmartServer
   BB = bestbuyServer.test(name)
   WM = WalmartServer.test(name)
   finJ['Results']=BB['BBlistings']
   finJ['Results'].extend(WM['WMlistings'])
   print("returning......",finJ)
   return finJ

if __name__ == '__main__':
   app.run(debug = True)

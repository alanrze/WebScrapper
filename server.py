from flask import Flask, redirect, url_for, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/success/<name>')
def success(name):
   finJ = {}
   finJ['Results']=[]
   import bestbuyServer
   import WalmartServer
   #temp = 'I THINK IT WORKS %s' % name
   BB = bestbuyServer.test(name)
   WM = WalmartServer.test(name)
   #dic['WM'] = WM
   #dic['BB'] = BB
   finJ['Results'].append(BB)
   finJ['Results'].append(WM)
   return finJ

if __name__ == '__main__':
   app.run(debug = True)

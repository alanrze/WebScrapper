from flask import Flask, redirect, url_for, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/success/<name>')
def success(name):
   import bestbuyServer
   """import WalmartServer
   temp = 'I THINK IT WORKS %s' % name
   BB = str(bestbuyServer.test(name))
   WM = str(WalmartServer.test(name))
   return(BB+'\n'+WM)"""
   return bestbuyServer.test(name)

if __name__ == '__main__':
   app.run(debug = True)

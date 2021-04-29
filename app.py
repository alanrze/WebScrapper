from flask import Flask, redirect, url_for, request
from flask_cors import CORS
import json
import threading

app = Flask(__name__)
CORS(app)
stores = 2
finJ={}

@app.route('/success/<name>')
def success(name):
   threads= []
   print("returning......",finJ)
   for i in range(stores):
      t = threading.Thread(target=switcher(name, i))
      t.daemon = True
      threads.append(t)
   for i in range(stores):
      threads[i].start()
   for i in range(stores):
      threads[i].join()
      
   print('HI')
   return finJ
finJ['Results']={}
def switcher(name, x):
   #finJ['Results'] = {'id':2, 'name': 'temp'}
   if(x==0):
      import bestbuyServer
      BB = bestbuyServer.test(name)
      print('HI')
      finJ['Results']=BB['BBlistings']
   elif(x==1):
      import WalmartServer
      WM = WalmartServer.test(name)
      print('HI1')
      finJ['Results'].extend(WM['WMlistings'])
   print(x)

if __name__ == '__main__':
   app.run(debug = True)
   

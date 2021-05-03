import re
import mechanicalsoup
import html
import urllib.parse
import json

def test(query):
    URL = "https://www.gamestop.com/search/?q=" + query
    browser = mechanicalsoup.StatefulBrowser(soup_config={'features':'lxml'}, user_agent='MechanicalSoup')
    browser.open(URL)
    page = browser.get_current_page()
    #print(page)
    results = page.find_all('div', attrs = {'class':'product-grid-tile-wrapper'})
    #print(results)
    finJ = {}
    finJ['GSlistings']=[]
    
    for x in results:
        dic = {}
        jsonRe = x.find('div', attrs = {'class':'pdp-link'})
        item = jsonRe['data-gtmdata'].split(',')
        #print(item)
        name = list(filter(lambda y: "name" in y, item))[0][8:-1]
        price = float(list(filter(lambda y: "price" in y, item))[0][25:-1])
        stock = list(filter(lambda y: "availability" in y, item))[0]
        if(stock.find('Not')!=-1):
            stock = "OOS"
        else:
            stock = "In Stock"
        #print(stock)
        link = 'https://www.gamestop.com'+str(x.find('a', attrs = {'class':'product-tile-link'})['href'])
        pic = str(x.find('img', attrs = {'class':'tile-image'})['data-src'])[:-12]
        #print(pic)
        
        dic['name']=name
        dic['price']=price
        dic['redirectURL']=link
        dic['pic']=pic
        dic['combo']=1
        dic['stock']=stock
        dic['store']="GameStop"
        finJ['GSlistings'].append(dic)
        
    print(finJ)    
    return(finJ)
    
#test("ps5")

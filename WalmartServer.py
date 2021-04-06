import re
import mechanicalsoup
import html
import urllib.parse
import json


def test(query):
    # Connect to duckduckgo
    URL = "https://www.walmart.com/search/?query=" + query
    browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')
    browser.open(URL)

    page = browser.get_current_page()
    resultsPrice = page.find_all('span', attrs={'class': 'price display-inline-block arrange-fit price price-main'})
    resultsName = page.find_all('a', attrs={'class': 'product-title-link line-clamp line-clamp-2 truncate-title'})
    resultsPics = page.find_all('img', attrs={'data-pnodetype': 'item-pimg'})

    #element1 = page.select('div.priceView-customer-price > span:first-child')

    #print(element1, resultsName, resultsPics)
    itrt = 0
    finJ = {}
    finJ['WMlistings']=[]
    #data = finJ['BBlistings']
    
    #print(resultsPrice, resultsName, resultsPics)
    
    for (x,y,z) in zip(resultsPics, resultsName, resultsPrice):
        priceStr = str(resultsPrice[itrt].text)
        strLenHalf = int((len(priceStr)/2))
        pictureLink = str(x['src'])
        dic = {}
        dic['name']=str(resultsName[itrt].text)
        dic['price']=priceStr[0:strLenHalf]
        dic['pic']=resultsPics[itrt]['src']
        #dic['redirectURL']=str(linkFin)
        dic['store']="Walmart"
        
        finJ['WMlistings'].append(dic)
        #print(x,y,z)
        itrt = itrt+1
        if(itrt>=5):
           break

    print()

    print(finJ)
    return finJ
    
    
#test("tv")

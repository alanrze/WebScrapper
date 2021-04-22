import re
import mechanicalsoup
import html
import urllib.parse
import json


def test(query):
    URL = "https://www.walmart.com/search/?grid=true&query=" + query
    browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')
    browser.open(URL)

    page = browser.get_current_page()
    itrt = 0
    finJ = {}
    finJ['WMlistings']=[]
    
    i=10
    results = page.find_all('li', attrs = {'class':'Grid-col'})
    print("BELOW")
    print("FIND", len(results))
    
    for x in results:
        dic = {}
        resultsRange = []
        resultsPrice = x.find('span' , attrs={'class' : 'price-main-block'})
        resultsName = x.find('a', attrs={'class': 'product-title-link line-clamp line-clamp-2 truncate-title'})
        resultsPics = x.find('img', attrs={'data-pnodetype': 'item-pimg'})
        resultsATC = x.find('button', attrs={'class': 'button stepper-toggle__bttn button--ghost'})
        resultsCOB = x.find('a', attrs={'class': 'button--choose-options'})
        linkStrt=x.find('a')
        linkFin="https://www.walmart.com/"+linkStrt['href']
        if(resultsPrice is None):
            continue
        
        print(resultsPrice.text)
        tempPrice = str(resultsPrice.text).split('$')
        print(tempPrice)
        if(len(tempPrice) == 5):
            dic['priceRange'] = True
            dic['price'] = float(tempPrice[1])
            dic['priceHigh'] = float(tempPrice[4])
        else:
            dic['priceRange'] = False
            dic['price'] = float(tempPrice[1])
        
        if(resultsATC is None and resultsCOB is None):
            dic['stock']="OOS"
            #print("OOS")
        else:
            dic['stock']="In Stock"
            #print("IS")
        
        dic['combo']=1
        dic['store']="Walmart"
        dic['name']=str(resultsName.text)
        dic['pic']=resultsPics['src']
        dic['redirectURL']=str(linkFin)
        
        print(dic)
        #if(itrt>=5):
        #   break
    

    print()

    print("FindJ", finJ)
    return finJ
    
    
test("tv")

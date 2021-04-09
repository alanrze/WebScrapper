import re
import mechanicalsoup
import html
import urllib.parse
import json

def test(query):
    URL = "https://www.bestbuy.com/site/searchpage.jsp?st=" + query
    browser = mechanicalsoup.StatefulBrowser(soup_config={'features':'lxml'}, user_agent='MechanicalSoup')
    browser.open(URL)
    page = browser.get_current_page()
    results = page.find_all('li', attrs = {'class':'sku-item'})

    itrt = 0
    finJ = {}
    finJ['BBlistings']=[]
    
    for x in results:
        dic = {}
        resultsName = x.find('div', attrs={'class': 'sku-title'})
        resultsPrice = x.select('div.priceView-customer-price > span:first-child')
        resultsStock = x.find('button', attrs={'class': 'add-to-cart-button'})
        resultsPics = x.find('img', attrs={'class':"product-image"})

        linkStrt=x.find('a')
        linkFin="https://www.bestbuy.com"+linkStrt['href']

        #pictureLink = str(resultsPics['src'])
        dic['name']=str(resultsName.text)
        dic['price']=str(resultsPrice[0].text)
        #dic['pic']=pictureLink[:-27]
        dic['redirectURL']=str(linkFin)
        
        if resultsPics is None:
            dic['pic']=[]
            resultsPics = x.find_all('div', attrs={'class': 'picture-wrapper'})
            for y in resultsPics:
                element = y.find('img')
                #print(resultsPics)
                #print(element['src'])
                #pics.append(element['src'])
                length = len(resultsPics)
                dic['combo']=length
                pictureLink=str(element['src'])
                dic['pic'].append(pictureLink[:-27])
        else:
            pictureLink = str(resultsPics['src'])
            dic['combo']=1
            dic['pic']=pictureLink[:-27]
            
        if(resultsStock is None):
            dic['stock']="OOS"
        if(resultsStock.text=="Sold Out" or resultsStock.text=="Out of Stock" or resultsStock.text=="Out Of Stock"):
            dic['stock']="OOS"
            #print("OOS")
        else:
            dic['stock']="In Stock"
            #print("IS")
        
        
        dic['store']="BestBuy"
        
        finJ['BBlistings'].append(dic)
        #print(x,y,z)
        itrt = itrt+1
        #if(itrt>=5):
        #   break   

    print()

    print(finJ)
    return finJ
    
    
#test("ps5")

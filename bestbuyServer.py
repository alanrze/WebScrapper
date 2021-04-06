import re
import mechanicalsoup
import html
import urllib.parse
import json


def test(query):
    # Connect to duckduckgo
    URL = "https://www.bestbuy.com/site/searchpage.jsp?st=" + query
    browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')
    browser.open(URL)

    page = browser.get_current_page()
    resultsPrice = page.find_all('div', attrs={'class': 'priceView-hero-price priceView-customer-price'})
    resultsName = page.find_all('h4', attrs={'class': 'sku-header'})
    resultsPics = page.find_all('img', attrs={'class':"product-image"})

    element1 = page.select('div.priceView-customer-price > span:first-child')

    #print(element1, resultsName, resultsPics)
    itrt = 0
    finJ = {}
    finJ['BBlistings']=[]
    #data = finJ['BBlistings']
    
    for (x,y,z) in zip(resultsPics, resultsName, element1):
        linkStrt=y.find('a')
        linkFin="https://www.bestbuy.com/"+linkStrt['href']
        pictureLink = str(x['src'])
        dic = {}
        dic['name']=str(y.text)
        dic['price']=str(z.text)
        dic['pic']=pictureLink[:-27]
        dic['redirectURL']=str(linkFin)
        dic['store']="BestBuy"
        
        finJ['BBlistings'].append(dic)
        #print(x,y,z)
        itrt = itrt+1
        if(itrt>=5):
           break

    print()

    print(finJ)
    return finJ
    
    
#test("3060ti")

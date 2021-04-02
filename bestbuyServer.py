from bs4 import BeautifulSoup
#from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

def test(query):
    print("Opening window....")
    chrome_options = Options()
    #chrome_options.add_argument("--no-startup-window")
    driver = webdriver.Chrome(options=chrome_options)
    print("Opened window....")

    URL = "https://www.bestbuy.com/site/searchpage.jsp?st=" + query

    print("Loading page....")
    driver.get(URL)


    soup = BeautifulSoup(driver.page_source, 'html.parser')

    print("Gathering listings....")

    resultsPrice = soup.findAll('div', attrs={'class': 'priceView-hero-price priceView-customer-price'})
    resultsName = soup.findAll('h4', attrs={'class': 'sku-header'})
    resultsPics = soup.findAll('img', attrs={'class':"product-image"})
    

    element1 = soup.select('div.priceView-customer-price > span:first-child')
    
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
    
    driver.quit()
    print(finJ)
    return finJ
    
#test("3060ti")

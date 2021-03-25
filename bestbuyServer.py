from bs4 import BeautifulSoup
#from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test(query):
    print("Opening window....")
    chrome_options = Options()
    #chrome_options.add_argument("--no-startup-window")
    driver = webdriver.Chrome(options=chrome_options)
    print("Opened window....")

    URL = "https://www.bestbuy.com/site/searchpage.jsp?st=" + query
    #URL = 'https://www.bestbuy.com/site/searchpage.jsp?st=computer+laptop&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys'

    #list1 = []
    #list2 = []
    #list3 = []
    finlist = []
    sublist = []

    print("Loading page....")
    driver.get(URL)
    #page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    print("Gathering listings....")

    resultsPrice = soup.findAll('div', attrs={'class': 'priceView-hero-price priceView-customer-price'})
    resultsName = soup.findAll('h4', attrs={'class': 'sku-header'})
    resultsPics = soup.findAll('img', attrs={'class':"product-image"})

    element1 = soup.select('div.priceView-customer-price > span:first-child')
    
    itrt = 0
    
    for (x,y,z) in zip(resultsPics, resultsName, element1):
        sublist.append(x['src'])
        sublist.append(y.text)
        sublist.append(z.text)
        finlist.append(sublist)
        sublist=[]
        itrt = itrt+1
        if(itrt>=5):
           break

    print()

    driver.quit()
    print(finlist)
    return finlist
    
#test("tv23")

    

import re
import mechanicalsoup
import html
import urllib.parse
import json

def test(query):
    URL = "https://www.officedepot.com/catalog/search.do?Ntt=" + query
    browser = mechanicalsoup.StatefulBrowser(soup_config={'features':'lxml'}, user_agent='MechanicalSoup')
    browser.open(URL)
    page = browser.get_current_page()
    #print(page)
    results = page.find_all('div', attrs = {'class':'sku_item'})
    #print(results)
    finJ = {}
    finJ['ODlistings']=[]
    
    for x in results:
        dic = {}
        name = x.find('div', attrs={'class': 'desc_text'})
        price = x.find('span', attrs={'class':'price_column right'})
        stock = x.find('div', attrs={'class':'oos_label'})
        if stock is None:
            dic['stock'] = "In Stock"
        else:
            dic['stock'] = "OOS"
        #print(stock)
        pic = x.find('img')
        #print(pic)
        link = x.find('a', attrs={'class':'med_txt'})
        
        dic['name']=str(name.text)[1:]
        dic['price']=price.text
        dic['redirectURL']='https://www.officedepot.com'+link['href']
        dic['pic']=pic['data-src']
        dic['combo']=1
        
        dic['store']="OfficeDepot"
        finJ['ODlistings'].append(dic)
        
    print(finJ)    
    return(finJ)
    
    
#test("rtx")

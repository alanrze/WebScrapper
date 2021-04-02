from bs4 import BeautifulSoup
#from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

finlist = []
sublist=[]

def test(query):
	print("Opening window....")
	driver = webdriver.Chrome()

	print("Opened window....")

	URL = "https://www.walmart.com/search/?query=" + query
	driver.get(URL)
	print("Loading page....")

	soup = BeautifulSoup(driver.page_source, 'html.parser')
	print("Gathering listings....")

	name = soup.findAll('a', attrs={'class': 'product-title-link line-clamp line-clamp-2 truncate-title'})
	price = soup.findAll('span', attrs={'class': 'price display-inline-block arrange-fit price price-main'})
	pics = soup.findAll('img', attrs={'data-pnodetype': 'item-pimg'})

	#print(name)
	#print(price)
	print()
	itrt = 0
	"""for i in range(5):
    		print(name[i].text)
    		print(price[i].text)
    		print(pics[i]['src'])
    		finlist.append(name[i].text)
    		finlist.append(price[i].text)
    		finlist.append(pics[i]['src'])
    		print()
    		print()
    	"""
	for (x,y,z) in (name,price,pics):
		sublist.append(pics[i]['src'])
		sublist.append(name[i].text)
		sublist.append(price[i].text)
		finlist.append(sublist)
		if(itrt>=5):
    			break
	
	driver.quit()
	return finlist
#test("tv22")

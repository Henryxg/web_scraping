import os
from unittest import result
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
driver = webdriver.Chrome("./chromedriver")
url="https://www.tripadvisor.com//"
urlprueba= "https://www.booking.com/searchresults.en-us.html?ss=Cuenca%2C+Ecuador&label=gog235jc-1DCAEoggI46AdIM1gDaEGIAQGYATG4ARnIAQzYAQPoAQH4AQKIAgGoAgO4Asjih5oGwAIB0gIkZGEzZDdiY2MtNmFiOS00OTQ4LWIwODEtMDg1ZTBmYjlkOTBk2AIE4AIB&sid=e53fd91033e453be1072170ead87e82a&aid=397594&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-926345&dest_type=city&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure"
time.sleep(2)
driver.get(urlprueba)
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
eq= soup.find_all('div',class_= 'a826ba81c4 fe821aea6c fa2f36ad22 afd256fc79 d08f526e0d ed11e24d01 ef9845d4b3 da89aeb942')
                               
resultado= []
for hotel in eq:
    url_re= hotel.find('a',class_= 'e13098a59f').attrs['href']
    re_hotel={}
    driver.get(url_re)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    comentarios= soup.find_all('div',class_= 'YibKl MC R2 Gi z Z BB pBbQr')
    re_hotel['nombre']=soup.find_all('h1',class_= 'QdLfr b d Pn')[0].next ##nombre del hotel
    com_byre,listas=[],[]
    incommet = dict()
    for i in comentarios:
        incommet=dict()
        com_byre = [i.text]+com_byre
        incommet['comentarioi']=i.text
        incommet['fechai'] = i.find_all('div',class_= 'cRVSd')[0].text
        listas= listas + [incommet]
    re_hotel['comentarios']= listas
    resultado= resultado + [re_hotel]
print(resultado)




page = requests.get(urlprueba)
soup = BeautifulSoup(page.content, 'html.parser')
#hoteles
eq= soup.find_all('div',class_= 'listing_title')



urlnext= "https://www.tripadvisor.com/Hotels-g677335-Ambato_Tungurahua_Province-Hotels.html"
page = requests.get(urlnext)
soup = BeautifulSoup(page.content, 'html.parser')
#hoteles
eq= soup.find_all('div',class_= 'listing_title')


print(eq)

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[]
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
print(name)


import os
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
#driver = webdriver.Chrome("./chromedriver")
driver = webdriver.Chrome("./chromedriver")
url="https://www.expedia.com//"
urlprueba= "https://www.expedia.com/Hotel-Search?adults=2&d1=2022-10-19&d2=2022-10-20&destination=Quito%2C%20Pichincha%2C%20Ecuador&endDate=2022-10-20&latLong=-0.220299%2C-78.511714&regionId=3623&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2022-10-19&theme=&useRewards=false&userIntent="
driver.get(urlprueba)
page = driver.page_source
#page = requests.get(urlprueba)
soup = BeautifulSoup(page, 'html.parser')
eq= soup.find_all('div',class_="uitk-card uitk-card-roundcorner-all uitk-card-has-primary-theme")
resultado= []
for hotel in eq:
    url_re= url +hotel.find('a',class_="uitk-card-link")['href']
    re_hotel={}
    page = requests.get(url_re)
    soup = BeautifulSoup(page.content, 'html.parser')
    comentarios= soup.find_all('div',class_= 'lazyload-wrapper')
    comentarios= soup.find_all('div',class_= 'uitk-card-placeholder uitk-card-placeholder-animate-from-light uitk-card-placeholder-ratio-1-3')
    #soup.find_all('div',class_= 'uitk-expando-peek-main') uitk-card-content-section uitk-card-content-section-border-block-end uitk-card-content-section-padded
    re_hotel['nombre']=soup.find_all('div',class_= 'uitk-spacing uitk-spacing-padding-small-blockend-four uitk-spacing-padding-large-blockstart-three')[0].text ##nombre del hotel
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





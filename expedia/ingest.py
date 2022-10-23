import os
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
#driver = webdriver.Chrome("./chromedriver")
driver = webdriver.Chrome("./chrome/chromedriver")
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
    h_registrado={}
    driver.get(url_re)
    time.sleep(20)
    driver.get(url_re)
    elem=driver.find_element("xpath",'//*[@id="app-layer-base"]/div/main/div/div/section/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div[1]/div/div[2]/div/button')
    elem.click()
    time.sleep(2)
    elem.click()
    time.sleep(2)
    try:
        come_click=driver.find_element("xpath",'//*[@id="app-layer-PropertyDetailsReviewsBreakdownDialog"]/div[2]/div/div[2]/div/div/div[2]/section/div[2]/button')
        come_click=driver.find_element("xpath",'//*[@id="app-layer-base"]/div/main/div/div/section/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div[1]/div/div[2]/div/button')
    except:
        pass
    come_click=driver.find_element("xpath",'//*[@id="navigation"]/div[1]/div/ul/li[6]/a')
    come_click.click()
    time.sleep(2)
    come_click=driver.find_element("xpath",'//*[@id="navigation"]/div[1]/div/ul/li[6]/a')
    come_click.click()
    time.sleep(2)
    try:
        all_coment=driver.find_element("xpath",'//*[@id="app-layer-PropertyDetailsReviewsBreakdownDialog"]/div[2]/div/div[2]/div/div/div[2]/section/div[2]/button')
    except:
        pass
    all_coment.click()
    time.sleep(2)
    page = driver.page_source
    soupcom = BeautifulSoup(page, 'html.parser')
    h_registrado['nombre']  =   soupcom.find('h1',class_= 'uitk-heading uitk-heading-3').text
    h_registrado['calificacion']  =   soupcom.find('h1',class_= 'uitk-heading uitk-heading-5 uitk-spacing uitk-spacing-padding-blockend-three').text
    h_registrado['direccion']  =   soupcom.find('h1',class_= 'uitk-text uitk-type-300 uitk-text-default-theme uitk-layout-flex-item uitk-layout-flex-item-flex-basis-full_width').text
    comentarios= soupcom.find_all('div',class_= 'uitk-card-content-section uitk-card-content-section-border-block-end uitk-card-content-section-padded')
    com_byre, hcomen=[],[]
    for comen in comentarios:
        incommet = dict()
        incommet['comentario'] = comen.find('div',class_= 'uitk-expando-peek uitk-spacing uitk-spacing-padding-blockstart-two').text
        incommet['compania'] = comen.find_all('div',class_= 'uitk-text uitk-type-300 uitk-text-default-theme')[0].text
        incommet['fechac'] = comen.find_all('div',class_= 'uitk-text uitk-type-300 uitk-text-default-theme')[1].text
        hcomen = hcomen + [incommet]
    h_registrado['comentarios']= hcomen
    resultado= resultado + [h_registrado]
print(resultado)



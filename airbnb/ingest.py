import os
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from selenium.webdriver.common.keys import Keys
import json 

driver = webdriver.Chrome("./chromedriver")
url="https://www.expedia.com//"
urlprueba= "https://www.airbnb.com/s/Quito--Pichincha--Ecuador/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=Quito%2C%20Pichincha&date_picker_type=calendar&place_id=ChIJn3xCAkCa1ZERclXvWOGRuUQ&flexible_date_search_filter_type=3&checkin=2022-10-28&checkout=2022-10-29&source=structured_search_input_header&search_type=autocomplete_click"
driver.get(urlprueba)
time.sleep(5)
page = driver.page_source
#page = requests.get(urlprueba)
soup = BeautifulSoup(page, 'html.parser')
eq = soup.find_all('div',class_="c1l1h97y dir dir-ltr")  
resultado= []

for hotel in eq:
    h_registrado={}
    
    try:
        url_re = 'https://www.airbnb.com/'+hotel.find('a',class_="ln2bl2p dir dir-ltr").attrs['href']
        time.sleep(4)
        h_registrado["descripccion"]=hotel.text
        h_registrado["link"]=url_re
       
        
    

    
        driver.get(url_re)
        time.sleep(2)
        page = driver.page_source
        try:
            veras=driver.find_element("xpath",'/html/body/div[11]/section/div/div/div[2]/div/div[1]/button')
            veras.click()
        except:
            pass
        time.sleep(2)

        try:
            page = driver.page_source
            soup = BeautifulSoup(page, 'html.parser') 
            h_registrado['nombre'] = soup.find('div',class_="_b8stb0").text
            h_registrado["precio"] = soup.find('div',class_="_ud8a1c").find('span',class_="_tyxjp1").text
            h_registrado["puntuacion_ge"] = soup.find('div',class_="_ud8a1c").find('span',class_="_12si43g").text
            
            time.sleep(0.5)
            elemet= driver.find_element("tag name", "body")
            for i in range(4):
                elemet.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.5)
            try: 
                met=driver.find_element("xpath",'//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/section/div[3]/div/div/div[6]/div/div[2]/div[2]/button')
                met.click()
            except:
                try:
                    met=driver.find_element("xpath",'//*[@id="site-content"]/div/div[1]/div[1]/div[1]/div/div/div/div/section/div[2]/div[1]/span[1]/span[3]/button')
                    met.click()
                except:
                    try:
                        met=driver.find_element("xpath",'//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/section/div[4]/button')
                        met.click()
                    except:
                        pass

        except:
            pass
            
        time.sleep(1)
        driver.page_source
        time.sleep(1)

        try:
            elemet= driver.find_element("tag name", "body")
            letm= driver.find_element("xpath",'//*[@id="reviews-search-input"]')
            letm.click()
            time.sleep(0.5)
            for i in range(4):
                elemet.send_keys(Keys.PAGE_DOWN)
                time.sleep(1)
            page = driver.page_source
            soup = BeautifulSoup(page, 'html.parser')

            comentarios = soup.find_all('div',class_="r1are2x1 dir dir-ltr")
        except:
            pass
        #comentarios = soup.find('div',class_="_162hp8xh")
        hcomen=[]
        for comen in comentarios:
            incommet = dict()
            incommet['comentario'] = comen.find('span', class_= 'll4r2nl dir dir-ltr').text
            incommet['fechac'] = comen.find('ol', class_= '_7h1p0g').text
            hcomen = hcomen + [incommet]
        h_registrado['comentarios']= hcomen
        resultado= resultado + [h_registrado]
    except:
        print('algo pasa con ' )



    

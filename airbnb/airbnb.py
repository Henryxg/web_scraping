from mimetypes import init
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from selenium.webdriver.common.keys import Keys
import json 


class Hotel_Airbnb():
    def __init__(self, link_hotel_ci):
        self.linkh= link_hotel_ci
        self.driver=  webdriver.Chrome("./chromedriver")

    def clickon(self, xxpad):
        try:
            veras= self.driver.find_element("xpath", xxpad )
            veras.click()
            time.sleep(0.5)
            return True
        except:
                print('problema en click en  ' + xxpad)
                return False
    
   
    def scrooll(self):
        elemet= self.driver.find_element("tag name", "body")
        for i in range(4):
            elemet.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
    

    def hotelesc(self ):
        try:
            self.driver.get(self.linkh)
            self.scrooll()
            time.sleep(3)
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser')
            eq = soup.find_all('div',class_="c1l1h97y dir dir-ltr") 
            return eq
        except:
            return False
    

    def inf_hotel(self, h_registrado, hotel):
        try:
            url_re = 'https://www.airbnb.com/'+hotel.find('a',class_="ln2bl2p dir dir-ltr").attrs['href']
            time.sleep(2)
            h_registrado["descripccion"]=hotel.text
            h_registrado["link"]=url_re
            ## ingresando al hotel
            self.driver.get(url_re)
            time.sleep(2)
           
            self.clickon('/html/body/div[11]/section/div/div/div[2]/div/div[1]/button')  # si existe el aununcio d etraducir
            
            time.sleep(2)
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser') 
            h_registrado['nombre'] = soup.find('div',class_="_b8stb0").text
            h_registrado["precio"] = soup.find('div',class_="_ud8a1c").find('span',class_="_tyxjp1").text
            h_registrado["puntuacion_ge"] = soup.find('div',class_="_ud8a1c").find('span',class_="_12si43g").text
            
            time.sleep(0.5)
            self.scrooll()
            sera_c = self.clickon( '//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/section/div[3]/div/div/div[6]/div/div[2]/div[2]/button')
            sera_c = self.clickon('//*[@id="site-content"]/div/div[1]/div[1]/div[1]/div/div/div/div/section/div[2]/div[1]/span[1]/span[3]/button') if sera_c == False else False
            sera_c = self.clickon( '//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/section/div[4]/button') if sera_c == False else False
            return h_registrado
                
        except:
                pass

    def open_hidenc(self):
            time.sleep(1)
            self.driver.page_source
            time.sleep(1)

            try:
                elemet= self.driver.find_element("tag name", "body")
                letm= self.driver.find_element("xpath",'//*[@id="reviews-search-input"]')
                letm.click()
                time.sleep(0.5)
                for i in range(4):
                    elemet.send_keys(Keys.PAGE_DOWN)
                    time.sleep(1)
            except:
                pass

    def get_comments(self):
      
        try:
            hcomen=[]
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser')

            comentarios = soup.find_all('div',class_="r1are2x1 dir dir-ltr")
            for comen in comentarios:
                incommet = dict()
                incommet['comentario'] = comen.find('span', class_= 'll4r2nl dir dir-ltr').text
                incommet['fechac'] = comen.find('ol', class_= '_7h1p0g').text
                hcomen = hcomen + [incommet]
            return hcomen
        except:
            print('algo pasa con ' )

    def ingest(self):
        resultado= []
        eq = self.hotelesc()
        for hotel in eq:
            h_registrado = {}
            h_registrado = self.inf_hotel( h_registrado, hotel)
            self.open_hidenc()
            hcomen = self.get_comments()
            h_registrado['comentarios']= hcomen
            resultado= resultado + [h_registrado]
        print('hola estoy aqui')
        json_object = json.dumps(resultado)
        with open("airbnb/sample-airbnb.json", "w") as outfile:
            outfile.write(json_object)


if __name__ == "__main__":
    urlprueba= "https://www.airbnb.com/s/Quito--Pichincha--Ecuador/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=Quito%2C%20Pichincha&date_picker_type=calendar&place_id=ChIJn3xCAkCa1ZERclXvWOGRuUQ&flexible_date_search_filter_type=3&checkin=2022-10-28&checkout=2022-10-29&source=structured_search_input_header&search_type=autocomplete_click"
    Hotel_Airbnb(urlprueba).ingest()
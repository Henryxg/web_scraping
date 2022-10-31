from mimetypes import init
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from selenium.webdriver.common.keys import Keys
import json 
import expedia_schema
import random

class Hotel_Expedia():
    def __init__(self, ciudad):
        self.schema = expedia_schema.Schemas().getSchema(ciudad)
        if self.schema == False:
            return print('ciudad no existe'+ ciudad) 

        self.linkh= self.schema['url'] 
        self.driver=  webdriver.Chrome("./chromedriver")
        self.url = "https://www.expedia.com//"
        
    def refresh(self):
        time.sleep(0.5)
        page = self.driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        return soup

    def get_clval(self, soupp, tip, etiqueta):
        if soupp.find(tip,class_= etiqueta) is not None:
            return soupp.find( tip ,class_= etiqueta)    #soupp.find( tip ,class_= etiqueta)
        else: 
            ''

    def clickon(self, xxpad):
        try:
            veras= self.driver.find_element("xpath", xxpad )
            veras.click()
            time.sleep(0.5)
            return True
        except:
                print('problema en click en  ' + xxpad)
                return False
    
   
    def scrooll(self,times):
        elemet= self.driver.find_element("tag name", "body")
        for i in range(times):
            elemet.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5+random.random())
    

    def hotelesc(self ):
        try:
            self.driver.get(self.linkh)
            self.scrooll(2)
            time.sleep(3)
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser')
            eq = soup.find_all('div',class_="uitk-spacing uitk-spacing-margin-blockstart-three") 
            return eq
        except:
            return False
    

    def inf_hotel(self, h_registrado, hotel):
        try:
            url_re = self.url +hotel.find('a',class_="uitk-card-link").attrs['href']
            self.driver.get(url_re)
            time.sleep(20)
            self.clickon('//*[@id="navigation"]/div[1]/div/ul/li[1]')
            time.sleep(2)
            soup= self.refresh()
            h_registrado["link"]  =  url_re
            h_registrado['nombre']  =  soup.find( 'h1' ,class_= 'uitk-heading uitk-heading-3').text  if   soup.find( 'h1' ,class_= 'uitk-heading uitk-heading-3') is not None else ''  # soup.find( 'h1' ,class_= 'uitk-heading uitk-heading-3')
            h_registrado['calificacion']  =   soup.find( 'h3' ,class_= 'uitk-heading uitk-heading-5 uitk-spacing uitk-spacing-padding-blockend-three').text[:3] if soup.find( 'h3' ,class_= 'uitk-heading uitk-heading-5 uitk-spacing uitk-spacing-padding-blockend-three') is not None else ''
            h_registrado['direccion']  =  soup.find( 'div' ,class_=  'uitk-text uitk-type-300 uitk-text-default-theme uitk-layout-flex-item uitk-layout-flex-item-flex-basis-full_width').text  if soup.find( 'div' ,class_=  'uitk-text uitk-type-300 uitk-text-default-theme uitk-layout-flex-item uitk-layout-flex-item-flex-basis-full_width') is not None else ''  
            self.scrooll(4)
            time.sleep(3)
            h_registrado["descripccion"]= self.get_clval( soup, 'div', 'uitk-text uitk-type-300 uitk-text-default-theme')
            
            self.scrooll(5)
            ## ingresando al hotel
          
            time.sleep(2)
           
            self.clickon('//*[@id="navigation"]/div[1]/div/ul/li[6]')  # si existe el aununcio d etraducir
            
            time.sleep(2)
            self.scrooll(2)

            soup= self.refresh()
            
            
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
            hcomen =[]

            soup = self.refresh()

            comentarios =  soup.find_all('div',class_="uitk-card-content-section uitk-card-content-section-border-block-end uitk-card-content-section-padded")
            for comen in comentarios:
                incommet = dict()
                incommet['comentario'] = self.get_clval( comen, 'div', 'uitk-expando-peek uitk-spacing uitk-spacing-padding-blockstart-two').text
                incommet['compania'] = self.get_clval( comen,'div', 'uitk-text uitk-type-300 uitk-text-default-theme')[0].text
                incommet['fechac'] = self.get_clval( comen,'div', 'uitk-text uitk-type-300 uitk-text-default-theme')[1].text
                hcomen = hcomen + [incommet]
            return hcomen
        except:
            print('algo pasa con ' )

    def ingest(self, ciud):
        resultado= []
        eq = self.hotelesc()
        for hotel in eq:
            h_registrado = {}
            h_registrado = self.inf_hotel( h_registrado, hotel)
            #self.open_hidenc()
            hcomen = self.get_comments()
            h_registrado['comentarios']= hcomen
            resultado= resultado + [h_registrado]
        print('hola estoy aqui')
        json_object = json.dumps(resultado)
        with open( ciud+"/sample-airbnb.json", "w") as outfile:
            outfile.write(json_object)


if __name__ == "__main__":
   
    ciudad= 'quito'
    Hotel_Expedia(ciudad).ingest('ambatov1')
    ciudades = ['quito']
from mimetypes import init
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from selenium.webdriver.common.keys import Keys
import json 


class Hotel_Tripadvisor():
    def __init__(self, link_hotel_ci):
        self.linkh= link_hotel_ci
        self.driver=  webdriver.Chrome("./chromedriver")
        self.url = "https://www.tripadvisor.com//"

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
        for i in range(2):
            elemet.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
    

    def hotelesc(self ):  
        try:
            self.driver.get(self.linkh)   
            self.scrooll()
            self.clickon('//*[@id="component_7"]/div/button')
            self.scrooll()
            time.sleep(3)
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser')
            eq = soup.find_all('div',class_="prw_rup prw_meta_hsx_responsive_listing ui_section listItem")  ## encuantra la lista de hoteles que hay que  prw_rup prw_meta_hsx_responsive_listing ui_section listItem
            return eq
        except:
            return False
    

    def inf_hotel(self, h_registrado, hotel):
        try:
            url_re = self.url + hotel.find('div',class_="listing_title").find('a',class_= 'property_title prominent')['href']
            time.sleep(2)
            h_registrado["descripccion"]=hotel.find('a',class_="review_count").text
            h_registrado["link"]=url_re
            ## ingresando al hotel
            self.driver.get(url_re)
            time.sleep(2)
           
            self.clickon('/html/body/div[11]/section/div/div/div[2]/div/div[1]/button')  # si existe el aununcio d etraducir
            
            time.sleep(2)
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser') 
            h_registrado['nombre'] = soup.find('h1',class_="QdLfr b d Pn").text         if soup.find('h1',class_="QdLfr b d Pn") is not None else ''
            h_registrado["precio"] = soup.find('div',class_="JPNOn b Wi").text          if soup.find('div',class_="JPNOn b Wi") is not None else ''
            h_registrado["direccion"] = soup.find('span',class_="fHvkI PTrfg").text     if soup.find('span',class_="fHvkI PTrfg") is not None else ''
            informacion = soup.find('div',class_="ui_columns MXlSZ")                   # if soup.find('h1',class_="QdLfr b d Pn") is not None else ''
            h_registrado["puntuacion"]= informacion.find('span',class_="uwJeR P").text  if informacion.find('span',class_="uwJeR P") is not None else ''
            h_registrado["descripcion"]= informacion.find('div',class_="fIrGe _T").text  if informacion.find('div',class_="fIrGe _T") is not None else ''
            h_registrado["calficacion"] = informacion.find('div',class_="kkzVG").text   if informacion.find('div',class_="kkzVG") is not None else ''
            time.sleep(0.5)
            self.scrooll()
            time.sleep(1.5)
            
            
            self.clickon('//*[@id="component_16"]/div/div[3]/div[1]/div[1]/div[4]/ul/li[1]') if self.clickon('//*[@id="component_15"]/div/div[3]/div[1]/div[1]/div[4]/ul/li[1]') !=True else None
            
            self.scrooll()
            
            time.sleep(0.5)
            self.scrooll()
            #sera_c = self.clickon( '//*[@id="dropdown_header"]/div[2]/div[2]/div[3]/span')   //*[@id="component_15"]/div/div[3]/div[3]/div/div[2]/span[2]/span/button
            #sera_c = self.clickon('//*[@id="ABOUT_TAB"]/div[2]/div[1]/div[1]/a/span[2]') if sera_c == False else False
            #sera_c = self.clickon( '//*[@id="component_3"]/div/div/div[1]/div[2]/a/span[2]') if sera_c == False else False
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

            comentarios = soup.find_all('div',class_="YibKl MC R2 Gi z Z BB pBbQr")
            for comen in comentarios:
                incommet = dict()
                incommet['comentario'] = comen.find('div', class_= 'fIrGe _T').text  if comen.find('div', class_= 'fIrGe _T') is not None else ''
                incommet['fechac'] = comen.find('div', class_= 'cRVSd').text[-9:] if comen.find('div', class_= 'cRVSd') is not None else ''
                incommet['calificacion']= comen.find('span', class_= 'ui_bubble_rating').attrs['class'][1] if comen.find('span', class_= 'ui_bubble_rating') is not None else ''
                incommet['p_location'] = comen.find('span', class_= 'RdTWF').text if comen.find('span', class_= 'RdTWF') is not None else ''
                incommet['p_n_contributions'] = comen.find('span', class_= 'yRNgz').text if comen.find('span', class_= 'yRNgz') is not None else ''
                hcomen = hcomen + [incommet]
            return hcomen
        except:
            print('algo pasa con ' )

    def ingest(self,ciudad):
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
        with open("tripadvisor/" +ciudad +"-tripad.json", "w") as outfile:
            outfile.write(json_object)


if __name__ == "__main__":
    #urlprueba= "https://www.tripadvisor.com/Hotels-g677335-Ambato_Tungurahua_Province-Hotels.html"
    urlprueba="https://www.tripadvisor.com/Hotels-g294308-Quito_Pichincha_Province-Hotels.html"
    Hotel_Tripadvisor(urlprueba).ingest('Ambato')


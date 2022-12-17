from mimetypes import init
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from selenium.webdriver.common.keys import Keys
import json 
import airbnb_schema
import random
import datetime as dt
import string 

class Hotel_Airbnb():
    def __init__(self, ciudad):
        self.schema = airbnb_schema.Schemas().getSchema(ciudad)
        if self.schema == False:
            return print('ciudad no existe'+ ciudad) 

        self.linkh= self.schema['url'] 

        self.servi= ciudad
        
        self.driver=  webdriver.Chrome("/home/henryx/prueba/web_scraping/chromedriver")
        self.url = "https://www.airbnb.com/"
        self.sito = 'expedia'
        self.ciudad = ciudad
        self.n_habitaciones= 2
        self.tipone = 'hotel'

    def clickon(self, xxpad):
        try:
            veras= self.driver.find_element("xpath", xxpad )
            veras.click()
            time.sleep(0.5)
            return True
        except:
                print('problema en click en  ' + xxpad)
                return False
    
    def refresh(self):
        time.sleep(0.5)
        page = self.driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        return soup

    def limpiesa(self, value, tipo):
        if tipo== 'fechac':
            full_month_format = "%B %Y"
            full_month_date= value.replace(',  · ,  · Last minute trip','')
            per=dt.datetime.strptime(full_month_date, full_month_format).strftime("%Y-%m-%d")
            return per 
        elif tipo== 'precio':
            value= ''.join(filter(lambda x: x.isdigit(), value))            
            return float(value)
        elif tipo== 'ppuntuacion': 
            value= ''.join(filter(lambda x: x.isdigit() or x=='.', value))
            value = value.replace(' ','')
            return float(value)
        
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
            time.sleep(3)
            eq = soup.find_all('div',class_="c1l1h97y dir dir-ltr") 
            return eq
        except:
            return False
    

    def inf_hotel(self, h_registrado, hotel):
        try:
            url_re = 'https://www.airbnb.com/'+hotel.find('a',class_="bn2bl2p dir dir-ltr").attrs['href']
            time.sleep(2)
            h_registrado['fecha_view'] = dt.datetime.today().strftime('%Y-%m-%d')
            h_registrado['tipo'] = self.tipone
            h_registrado["sitio_web"]  =  url_re
            h_registrado["descripccion"]=hotel.text
            
            
            ## ingresando al hotel
            self.driver.get(url_re)
            time.sleep(2)
           
            self.clickon('/html/body/div[11]/section/div/div/div[2]/div/div[1]/button')  # si existe el aununcio d etraducir
            self.clickon('/html/body/div[10]/section/div/div/div[2]/div/div[1]/button')
            time.sleep(2)
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser') 
            h_registrado['nombre_id'] = soup.find('div',class_="_b8stb0").text
            h_registrado["precio"] = self.limpiesa( soup.find('div',class_="_ud8a1c").find('span',class_="_tyxjp1").text, 'precio') if soup.find('div',class_="_ud8a1c").find('span',class_="_tyxjp1") is not None else ''
            h_registrado["precio"] = self.limpiesa( soup.find('div',class_="_ati8ih").find('span',class_="_1y74zjx").text , 'precio') if h_registrado["precio"]=='' and soup.find('div',class_="_ati8ih").find('span',class_="_1y74zjx") is not None else h_registrado["precio"]
            h_registrado["puntuacion"] = self.limpiesa( soup.find('div',class_="_ud8a1c").find('span',class_="_12si43g").text ,'ppuntuacion') if soup.find('div',class_="_ud8a1c").find('span',class_="_12si43g") is not None else ''
            h_registrado["ciudad"]=self.ciudad
            h_registrado["n_habitaciones"]= self.n_habitaciones
            time.sleep(0.5)
            self.scrooll()
            sera_c = self.clickon( '//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/section/div[3]/div/div/div[6]/div/div[2]/div[2]/button')
            sera_c = self.clickon('//*[@id="site-content"]/div/div[1]/div[1]/div[1]/div/div/div/div/section/div[2]/div[1]/span[1]/span[3]/button') if sera_c == False else False
            sera_c = self.clickon( '//*[@id="site-content"]/div/div[1]/div[4]/div/div/div/div[2]/section/div[4]/button') if sera_c == False else False
            return h_registrado
                
        except:
                return {}

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

    def get_comments(self,hnombre):
      
        try:
            hcomen=[]
            time.sleep(2)
            self.clickon('/html/body/div[10]/section/div/div/div[2]/div/div[3]/div/div/div/div/section/div/div[2]/div[1]/div/div/label/div/div/input')
            self.scrooll()
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser')

            comentarios = soup.find_all('div',class_="r1are2x1 dir dir-ltr")
            for comen in comentarios:
                incommet = dict()
                incommet['nombreh_id']= hnombre
                incommet['comentario'] = comen.find('span', class_= 'll4r2nl dir dir-ltr').text if comen.find('span', class_= 'll4r2nl dir dir-ltr') is not None else ''
                incommet['fechac'] = self.limpiesa(comen.find('ol', class_= '_7h1p0g').text,'fechac') if comen.find('ol', class_= '_7h1p0g') is not None else ''
                hcomen = hcomen + [incommet]
            return hcomen
        except:
            print('algo pasa con ' )
            return {}

    def ingest(self,ciudad):
        resultado= []
        eq = self.hotelesc()
        for hotel in eq:
            h_registrado = {}
            
            h_registrado = self.inf_hotel( h_registrado, hotel)
            #self.open_hidenc()
            hcomen = self.get_comments(h_registrado['nombre_id']) if 'nombre_id' in h_registrado else []
            if hcomen!=[]:
                h_registrado['comentarios']= hcomen 
            else:
                print("no hay cooemtarios en hotel")
                h_registrado = {}
            
            resultado= resultado + [h_registrado] if h_registrado!={} else resultado
           

        print('hola estoy aqui')
        json_object = json.dumps(resultado)
        with open("airbnb/basejson/" +ciudad +"_airbnb.json", "w") as outfile:
            outfile.write(json_object)


if __name__ == "__main__":
    ciudades=  ['guayaquil','ambato','ibarra','loja','manta','quito']
    for ciudad in ciudades:
        Hotel_Airbnb(ciudad).ingest(ciudad)
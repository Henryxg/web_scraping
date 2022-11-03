from mimetypes import init
import os
from string import punctuation
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from selenium.webdriver.common.keys import Keys
import json 
import booking_schema
import datetime as dt
import string 


class Hotel_booking():
    def __init__(self, ciudad):
        self.schema = booking_schema.Schemas().getSchema(ciudad)
        self.linkh= self.schema['url']
        self.driver=  webdriver.Chrome("./chromedriver")
        self.url = "https://www.booking.com/"
       
        self.sito = 'booking'
        self.ciudad = ciudad
        self.n_habitaciones= 2


    def clickon(self, xxpad):
        try:
            veras= self.driver.find_element("xpath", xxpad )
            veras.click()
            time.sleep(0.5)
            return True
        except:
                print('problema en click en  ' + xxpad)
                return False
    
   
    def scrooll(self, times):
        elemet= self.driver.find_element("tag name", "body")
        for i in range(times):
                elemet.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.5)
    
    def refresh(self):
        page = self.driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        return soup

    def hotelesc(self ):  
        try:
            self.driver.get(self.linkh)  
            time.sleep(10) 
            self.scrooll(4)
            self.clickon('//*[@id="component_7"]/div/button')
            self.scrooll(2)
            time.sleep(3)
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser')
            eq = soup.find_all('div',class_="b978843432")  ## encuantra la lista de hoteles que hay que  prw_rup prw_meta_hsx_responsive_listing ui_section listItem
            return eq
        except:
            return False
    
    def limpiesa(self, value, tipo):
        if tipo== 'fechacom':
            full_month_format = "%B %Y"
            full_month_date= value
            per=dt.datetime.strptime(full_month_date, full_month_format).strftime("%Y-%m-%d")
            return per 

    def inf_hotel(self, h_registrado, hotel):
        try:
            url_re = hotel.find('a',class_="e13098a59f")['href']
            time.sleep(2)
            h_registrado["sitio_web"]=url_re
            ## ingresando al hotel
            time.sleep(2)
            self.driver.get(url_re)
            time.sleep(2)
           
            self.clickon('/html/body/div[11]/section/div/div/div[2]/div/div[1]/button')  # si existe el aununcio d etraducir
           
            self.scrooll(7)
            
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser')  
            h_registrado['tipo'] = 'hotel'
            h_registrado['fecha_view'] = dt.datetime.today().strftime('%Y-%m-%d')
            h_registrado["descripccion"]=soup.find('div',id='property_description_content').text.replace('\n', '') if soup.find('div',id='property_description_content') is not None else ''
            h_registrado['nombre_id'] = soup.find('h2',class_='d2fee87262 pp-header__title').text    if soup.find('h2',class_='d2fee87262 pp-header__title') is not None else ''
            h_registrado["precio"] = float(soup.find('span',class_='prco-valign-middle-helper').text[3:][:-1].replace('$',''))          if soup.find('span',class_='prco-valign-middle-helper') is not None else ''
            h_registrado["direccion"] = soup.find('p',class_='address address_clean').text.replace('\n','')    if soup.find('p',class_='address address_clean') is not None else ''
            
            informacion =  soup.find('div',class_='hp-social_proof reviews-snippet-sidebar hp-social-proof-review_score') if soup.find('div',class_='hp-social_proof reviews-snippet-sidebar hp-social-proof-review_score') is not None else None
            #hp-social_proof reviews-snippet-sidebar


            h_registrado["puntuacion"]= float(informacion.find('div', class_='b5cd09854e d10a6220b4').text)/2  if informacion.find('div',class_="b5cd09854e d10a6220b4") is not None else ''
            h_registrado["calficacion_tx"] = informacion.find('span', class_='b5cd09854e f0d4d6a2f5 e46e88563a').text   if informacion.find('span',class_="b5cd09854e f0d4d6a2f5 e46e88563a") is not None else ''
            h_registrado["ciudad"]=self.ciudad
            h_registrado["n_habitaciones"]= self.n_habitaciones
           
            
            if h_registrado["puntuacion"]=='' :
                self.scrooll(7)
                soup = self.refresh()  
                informacion =  soup.find('div',class_='hp-social_proof reviews-snippet-sidebar hp-social-proof-review_score')
                h_registrado["puntuacion"]= long(informacion.find('div', class_='b5cd09854e d10a6220b4').text )/2 if informacion.find('div',class_="b5cd09854e d10a6220b4") is not None else ''
                h_registrado["calficacion_tx"] = informacion.find('span', class_='b5cd09854e f0d4d6a2f5 e46e88563a').text   if informacion.find('span',class_="b5cd09854e f0d4d6a2f5 e46e88563a") is not None else ''
            time.sleep(0.5)
            self.scrooll(2)
            
            de = self.clickon('//*[@id="guest-featured_reviews__horizontal-block"]/div[3]/div[9]/div/div/div/button')
            de = self.clickon('//*[@id="guest-featured_reviews__horizontal-block"]/div[3]/div[8]/div/div/div/button/span') if de==False else self.clickon('//*[@id="guest-featured_reviews__horizontal-block"]/div[2]/div[8]/div/div/button') 
            time.sleep(1)
            self.scrooll(2)
            self.clickon('//*[@id="review_sort"]')
            time.sleep(0.5)
            self.clickon('//*[@id="review_sort"]/option[2]')
            self.scrooll(2)
            time.sleep(1.5)
            
            
             
            return h_registrado
                
        except:
                 h_registrado = {}
                 return h_registrado
            

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

    def get_comments(self, hnombre):
      
        try:
            hcomen=[]
            soup = self.refresh()
            comentarios = soup.find_all('li',class_="review_list_new_item_block")
            for i in range(2):
                for comen in comentarios:
                    incommet = dict()
                    incommet['nombreh_id']= hnombre 
                    incommet['p_comentario'] = comen.find('span', class_= 'c-review__body').text  if comen.find('span', class_= 'c-review__body') is not None else ''
                    subcomen= comen.find('h3', class_= 'c-review-block__title c-review__title--ltr').text  if comen.find('h3', class_= 'c-review-block__title c-review__title--ltr') is not None else ''
                    incommet['p_comentario'] = subcomen.replace('\n','') if incommet['p_comentario'] == 'There are no comments available for this review' else incommet['p_comentario']+ subcomen
                    coments= comen.find_all('p', class_= 'c-review__inner c-review__inner--ltr') if comen.find_all('p', class_= 'c-review__inner c-review__inner--ltr') is not None else 3
                    if len(coments)==2:
                        
                        subscomen = coments[1].find('span', class_= 'c-review__body').text  if comen.find('span', class_= 'c-review__body') is not None else ''
                        incommet['p_comentario']= incommet['p_comentario']+ ' ' +subscomen.replace('\n',' ')
                    
                    incommet['p_fecha_comen'] = comen.find('span', class_= 'c-review-block__date').text.replace('\n','') if comen.find('span', class_= 'c-review-block__date') is not None else ''
                    incommet['p_fecha_comen'] = self.limpiesa(incommet['p_fecha_comen'], 'fechacom')
                    incommet['p_puntuacion']= float(comen.find('div', class_= 'bui-review-score__badge').text.replace(' ','') )/2 if comen.find('div', class_= 'bui-review-score__badge') is not None else ''
                    incommet['p_pais_de_origen'] = comen.find('span', class_= 'bui-avatar-block__subtitle').text.replace('\n','') if comen.find('span', class_= 'bui-avatar-block__subtitle') is not None else ''
                
                    hcomen = hcomen + [incommet]
                
                self.clickon('//*[@id="review_list_page_container"]/div[4]/div/div[1]/div/div[2]/div/div[2]')
                self.scrooll(2)
                soup = self.refresh()
                comentarios = soup.find_all('li',class_="review_list_new_item_block")        
                
            return hcomen
        except:
            print('algo pasa con ' )

    def ingest(self,ciudad):
        resultado= []
        eq = self.hotelesc()
        for hotel in eq[2:]:
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
        with open("booking/basejson/" +ciudad +"_booking.json", "w") as outfile:
            outfile.write(json_object)


if __name__ == "__main__":
  
    ciudades = ['ibarra']
    for i in ciudades:
        ciudad= i
        Hotel_booking(ciudad).ingest(ciudad+'v2')

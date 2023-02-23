from mimetypes import init
import os
from socket import TIPC_NODE_SCOPE
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from selenium.webdriver.common.keys import Keys
import json 
import expedia_schema
import random
import datetime as dt
import string 

class Hotel_Expedia():
    def __init__(self, ciudad):
        self.schema = expedia_schema.Schemas().getSchema(ciudad)
        if self.schema == False:
            return print('ciudad no existe'+ ciudad) 

        self.linkh= self.schema['url'] 
        self.driver=  webdriver.Chrome("./chromedriver")
        self.url = "https://www.expedia.com//"
        self.sito = 'expedia'
        self.ciudad = ciudad
        self.n_habitaciones= 2
        self.tipone = 'hotel'
        
    def refresh(self):
        time.sleep(0.5)
        page = self.driver.page_source
        soup = BeautifulSoup(page, 'html.parser')
        return soup

    def limpiesa(self, value, tipo):
        if tipo== 'fechacom':
            dic_moth= {"ene":"january", "feb":"february", "mar":"march", "abr":"april", "may":"may", "jun":"june", "jul":"july", "ago":"august", "sept":"september", "octubre":"oct", "novi":"november" , "dic":"december"}
            value= value.replace(',','')
            full_month_format = "%b %d %Y"
            full_month_date= value.replace('dic','dec').replace('sept','sep').replace('ago','aug')
            per=dt.datetime.strptime(full_month_date, full_month_format).strftime("%Y-%m-%d") 
            return per 
        elif tipo== 'precio':
            value= ''.join(filter(lambda x: x.isdigit(), value))            
            return float(value)
        elif tipo== 'ppuntuacion': 
            value= ''.join(filter(lambda x: x.isdigit(), value))
            value = value.replace(' ','')
            return float(value)

    def clickon(self, xxpad):
        try:
            veras= self.driver.find_element("xpath", xxpad )
            veras.click()
            time.sleep(0.5)
            return True
        except:
                #print('problema en click en  ' + xxpad)
                return False
    
   
    def scrooll(self,times):
        elemet= self.driver.find_element("tag name", "body")
        for i in range(times):
            elemet.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5+random.random())
    def scrooll_up(self,times):
        elemet= self.driver.find_element("tag name", "body")
        for i in range(times):
            elemet.send_keys(Keys.PAGE_UP)
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
    

    def inf_hotel(self, h_registrado, hotel,i):
        try:
            url_re = self.url +hotel.find('a',class_="uitk-card-link").attrs['href']
            self.driver.get(url_re)
            time.sleep(30) if i==1 else None
            self.clickon('//*[@id="navigation"]/div[1]/div/ul/li[1]')
            self.clickon('/html/body/div[2]/div[1]/div/div/main/div/div/section/div[1]/div[1]/div[1]/div/div[2]/div[2]/section/div/div/div/div[1]/div/ul/li[1]/a')
            time.sleep(2)
            soup= self.refresh()
            h_registrado['fecha_view'] = dt.datetime.today().strftime('%Y-%m-%d')
            h_registrado['tipo'] = self.tipone
            h_registrado["sitio_web"]  =  url_re
            h_registrado['nombre_id']  =  soup.find( 'h1' ,class_= 'uitk-heading uitk-heading-3').text  if   soup.find( 'h1' ,class_= 'uitk-heading uitk-heading-3') is not None else ''  # soup.find( 'h1' ,class_= 'uitk-heading uitk-heading-3')
            h_registrado['nombre_id']  =  soup.find( 'h1' ,class_= 'uitk-heading uitk-heading-4').text  if   h_registrado['nombre_id'] == '' is not None else h_registrado['nombre_id']  # soup.find( 'h1' ,class_= 'uitk-heading uitk-heading-3')
            precio_piv= soup.find( 'div' ,class_= 'uitk-spacing uitk-spacing-padding-block-half') if soup.find( 'div' ,class_= 'uitk-spacing uitk-spacing-padding-block-half') is not None else None
            preciotofl= precio_piv.find( 'div' ,class_= 'uitk-text uitk-type-300 uitk-text-default-theme is-visually-hidden') if precio_piv.find( 'div' ,class_= 'uitk-text uitk-type-300 uitk-text-default-theme is-visually-hidden') is not None else ''
            h_registrado['precio']= self.limpiesa(preciotofl.text, 'precio') if preciotofl!= '' else ''
            time.sleep(0.5)
            soup= self.refresh()
            h_registrado['puntuacion']  =   float(soup.find( 'div' ,class_= 'uitk-layout-flex uitk-layout-flex-align-items-center uitk-card uitk-card-roundcorner-all uitk-card-has-border uitk-card-has-primary-theme').text[:3])/2 if soup.find( 'div' ,class_= 'uitk-layout-flex uitk-layout-flex-align-items-center uitk-card uitk-card-roundcorner-all uitk-card-has-border uitk-card-has-primary-theme') is not None else ''
            h_registrado['puntuacion'] = float(soup.find( 'h3' ,class_= 'uitk-heading uitk-heading-5 uitk-spacing uitk-spacing-padding-blockend-three').text[:3]) if h_registrado['puntuacion']=='' and soup.find( 'h3' ,class_= 'uitk-heading uitk-heading-5 uitk-spacing uitk-spacing-padding-blockend-three') is not None else ''
            h_registrado['direccion']  =  soup.find( 'div' ,class_=  'uitk-text uitk-type-300 uitk-text-default-theme uitk-layout-flex-item uitk-layout-flex-item-flex-basis-full_width').text  if soup.find( 'div' ,class_=  'uitk-text uitk-type-300 uitk-text-default-theme uitk-layout-flex-item uitk-layout-flex-item-flex-basis-full_width') is not None else ''  
            self.scrooll(4)
            self.clickon('/html/body/div[2]/div[1]/div/div/main/div/div/section/div[1]/div[1]/div[1]/div/div[2]/div[2]/section/div/div/div/div/div/ul/li[3]/a') 
            time.sleep(3)
            soup= self.refresh()
            h_registrado["descripcion"]= soup.find( 'div' ,id= 'Location').find('div' ,class_=  'uitk-text uitk-type-300 uitk-text-default-theme').text if soup.find( 'div' ,id= 'Location') is not None else ''
            h_registrado["ciudad"]=self.ciudad
            h_registrado["n_habitaciones"]= self.n_habitaciones
            self.scrooll(5)
            ## ingresando al hotel
            
          
            time.sleep(2)
            self.scrooll(12)
            self.scrooll_up(1)
            see=self.clickon('/html/body/div[2]/div[1]/div/div/main/div/div/section/div[1]/div[1]/div[1]/div/div[3]/div[19]/div/div/div/div/div[2]/div/button')  # si existe el aununcio d etraducir
            see= self.clickon('/html/body/div[2]/div[1]/div/div/main/div/div/section/div[1]/div[1]/div[1]/div/div[3]/div[19]/div/div/div/div/div[2]/div/button')
            self.clickon('/html/body/div[2]/div[1]/div/div[1]/main/div/div/section/div[1]/div[1]/div[1]/div/div[3]/div[19]/div/div/div/div/div[2]/div')
            time.sleep(2)
            self.scrooll(3)

            soup= self.refresh()
            
            
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
            hcomen =[]
            soup = self.refresh()
            self.clickon('/html/body/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/select')
            self.clickon('/html/body/div[2]/div[1]/div/div/main/div/div/section/div[1]/div[1]/div[1]/div/div[3]/div[19]/div/div/div/div/div[2]/div')
            time.sleep(2)
            self.clickon('/html/body/div[2]/div[1]/div/div[1]/main/div/div/section/div[1]/div[1]/div[1]/div/div[3]/div[19]/div/div/div/div/div[2]/div/button')
            self.clickon('/html/body/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div/select/option[2]')
            time.sleep(2)
            self.scrooll(2)
            self.clickon('/html/body/div[2]/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/section/div[2]/button')
            self.scrooll(2)
            soup = self.refresh()
             #soup.find_all('div',class_="uitk-card-content-section uitk-card-content-section-border-block-end uitk-card-content-section-padded")
            comentarios =  soup.find('div', id="app-layer-infosite-reviews").find_all('div',class_="uitk-card-content-section uitk-card-content-section-border-block-end uitk-card-content-section-padded")
            for comen in comentarios:
                try:
                    incommet = dict()
                    incommet['nombreh_id']= hnombre 
                    incommet['comentario'] = comen.find('div',class_= 'uitk-expando-peek uitk-spacing uitk-spacing-padding-blockstart-two').text if comen.find('div',class_= 'uitk-expando-peek uitk-spacing uitk-spacing-padding-blockstart-two') is not None else ''
                    subcom= comen.find('h4',class_= 'uitk-heading uitk-heading-5').text[4:] if comen.find('h4',class_= 'uitk-heading uitk-heading-5') is not None else ''
                    incommet['comentario']=  subcom+ ' '+ incommet['comentario'] 
                    incommet['p_puntuacion'] = self.limpiesa(comen.find('h4',class_= 'uitk-heading uitk-heading-5').text[:2], 'ppuntuacion') if comen.find('h4',class_= 'uitk-heading uitk-heading-5') is not None else ''
                    incommet['p_fecha_comen'] = self.limpiesa(comen.find('span', itemprop= "datePublished").text, 'fechacom') if comen.find('span', itemprop= "datePublished") is not None else ''
                #incommet['p_acompanado'] = self.limpiesa(comen.find('span', itemprop= "datePublished").text, 'fechacom') if comen.find('span', itemprop= "datePublished") is not None else ''
                    hcomen = hcomen + [incommet]
                except:
                    pass
            return hcomen
        except:
            print('algo pasa con comentarios' )

    def ingest(self, ciudad):
        resultado= []
        eq = self.hotelesc()[:20]
        i=1
        for hotel in eq:
            h_registrado = {}
            
            h_registrado = self.inf_hotel( h_registrado, hotel, i)
            #self.open_hidenc()
            hcomen = self.get_comments(h_registrado['nombre_id']) if 'nombre_id' in h_registrado else []
            if hcomen!=[]:
                h_registrado['comentarios']= hcomen 
            else:
                print("no hay cooemtarios en hotel")
                h_registrado = {}
            
            resultado= resultado + [h_registrado] if h_registrado!={} else resultado
            i+=1

        print('hola estoy aqui')
        json_object = json.dumps(resultado)
        with open("expedia/basejson/" +ciudad +"_expedia.json", "w") as outfile:
            outfile.write(json_object)


if __name__ == "__main__":
    #ciudades = ['guayaquil','ambato','ibarra','loja','manta','quito']
    ciudades = ['ambato']
    for i in ciudades:
        ciudad= i
        Hotel_Expedia(ciudad).ingest(ciudad+'v3')
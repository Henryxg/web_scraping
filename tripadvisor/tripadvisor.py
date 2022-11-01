from mimetypes import init
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from selenium.webdriver.common.keys import Keys
import json 
import tripadvisor_schema
import datetime as dt
import string 

class Hotel_Tripadvisor():
    def __init__(self, ciudad):
        self.schema = tripadvisor_schema.Schemas().getSchema(ciudad)
        if self.schema == False:
            return print('ciudad no existe'+ ciudad) 

        self.linkh= self.schema['url'] 
        self.driver=  webdriver.Chrome("./chromedriver")
        self.url = "https://www.tripadvisor.com//"
        self.sito = 'tripadvisor'
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
    
   
    def scrooll(self):
        elemet= self.driver.find_element("tag name", "body")
        for i in range(2):
            elemet.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
    

    def hotelesc(self ):  
        try:
            self.driver.get(self.linkh)  
            time.sleep(2) 
            self.scrooll()
            self.clickon('//*[@id="component_7"]/div/button')
            self.scrooll()
            time.sleep(2)
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser')
            eq = soup.find_all('div',class_="prw_rup prw_meta_hsx_responsive_listing ui_section listItem")  ## encuantra la lista de hoteles que hay que  prw_rup prw_meta_hsx_responsive_listing ui_section listItem
            return eq
        except:
            return False
    def limpiesa(self, value, tipo):
        if tipo== 'numero':
            value= ''.join(filter(lambda x: x.isdigit() or x=='-', value))
            value = value.split('-')
            a,b= int(value[0]) , int(value[1])            
            return (a+b)/2 
        elif tipo == 'burble':
            dic_val= {'bubble_10':1,'bubble_20':2, 'bubble_30': 3, 'bubble_40':4, 'bubble_50':5}
            return dic_val[value]
        elif tipo == 'fecha':
            full_month_format = "%B %Y"
            full_month_date= value
            per=dt.datetime.strptime(full_month_date, full_month_format).strftime("%Y-%m-%d")
            return per
        elif tipo == 'p_fecha_comen':
            valuea= value
            month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Yesterday', 'Today']
            yearl = ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']
            value = ' '.join(list(filter(lambda x: x  in month or x in yearl, valuea.split())))
            valub = list(filter(lambda x: (x in month or x in yearl or x.isdigit()), valuea.split()))
            if  len(value)==3:
                value= valub[1]+' '+valub[0]+ ' 2022'
                full_month_date = value
                full_month_format = "%d %b %Y"
                return dt.datetime.strptime(full_month_date, full_month_format).strftime("%Y-%m-%d")
            elif value == 'Today':
                return dt.datetime.today().strftime('%Y-%m-%d')

            elif  value == 'Yesterday':
                return (dt.datetime.today()-dt.timedelta(days=1)).strftime('%Y-%m-%d')

            elif value != 'Yesterday':
                full_month_date= value
                full_month_format = "%b %Y"
                return dt.datetime.strptime(full_month_date, full_month_format).strftime("%Y-%m-%d")
            
            
            




    def inf_hotel(self, h_registrado, hotel):
        try:
            url_re = self.url + hotel.find('div',class_="listing_title").find('a',class_= 'property_title prominent')['href']
            time.sleep(2)
            #h_registrado["descripccion"]=hotel.find('a',class_="review_count").text
            h_registrado["link"]=url_re
            ## ingresando al hotel
            time.sleep(2)
            self.driver.get(url_re)
            time.sleep(2)
           
            self.clickon('/html/body/div[11]/section/div/div/div[2]/div/div[1]/button')  # si existe el aununcio d etraducir
            self.scrooll()
            time.sleep(1)
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser')  
            h_registrado['tipo'] = 'hotel'
            h_registrado['fecha_view'] = dt.datetime.today().strftime('%Y-%m-%d')
            h_registrado['nombre_id'] = soup.find('h1',id='HEADING').text     if soup.find('h1',id='HEADING') is not None else ''
            h_registrado["precio"] = soup.find('td',class_='IhqAp Ci').text   if soup.find('td',class_='IhqAp Ci') is not None else ''
            h_registrado["precio"] = soup.find('div',class_='IhqAp Ci').text if h_registrado["precio"]=='' and soup.find('div',class_='IhqAp Ci') is not None else h_registrado["precio"]
            h_registrado["precio"] = self.limpiesa( h_registrado["precio"] , 'numero')

            h_registrado["direccion"] = soup.find('span',class_="fHvkI PTrfg").text     if soup.find('span',class_="fHvkI PTrfg") is not None else ''
            informacion = soup.find('div',class_="ui_columns MXlSZ")                   # if soup.find('h1',class_="QdLfr b d Pn") is not None else ''
            h_registrado["puntuacion"]= float(informacion.find('span',class_="uwJeR P").text)  if informacion.find('span',class_="uwJeR P") is not None else ''
            h_registrado["descripcion"]= informacion.find('div',class_="fIrGe _T").text  if informacion.find('div',class_="fIrGe _T") is not None else ''
            h_registrado["calficacion_tx"] = informacion.find('div',class_="kkzVG").text   if informacion.find('div',class_="kkzVG") is not None else ''
            h_registrado["sitio_web"]=url_re
            h_registrado["ciudad"]=self.ciudad
            h_registrado["n_habitaciones"]= self.n_habitaciones
        

            time.sleep(0.5)
            self.clickon('//*[@id="component_16"]/div/div[3]/div[1]/div[1]/div[4]/ul/li[1]') if self.clickon('//*[@id="component_15"]/div/div[3]/div[1]/div[1]/div[4]/ul/li[1]') !=True else None
            self.scrooll()
            time.sleep(1.5)
            
            
            self.clickon('//*[@id="component_16"]/div/div[3]/div[1]/div[1]/div[4]/ul/li[1]') if self.clickon('//*[@id="component_15"]/div/div[3]/div[1]/div[1]/div[4]/ul/li[1]') !=True else None
            
            self.scrooll()
            self.clickon('//*[@id="component_16"]/div/div[3]/div[1]/div[1]/div[4]/ul/li[1]') if self.clickon('//*[@id="component_15"]/div/div[3]/div[1]/div[1]/div[4]/ul/li[1]') !=True else None
            time.sleep(0.5)
            self.scrooll()
     
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

    def get_comments(self, hnombre):
      
        try:
            hcomen=[]
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser')

            comentarios = soup.find_all('div',class_="YibKl MC R2 Gi z Z BB pBbQr")
            for comen in comentarios:
                try:
                    incommet = dict()
                    incommet['nombreh_id']= hnombre 
                    incommet['p_comentario'] = comen.find('div', class_= 'fIrGe _T').text  if comen.find('div', class_= 'fIrGe _T') is not None else ''
                    incommet['p_fecha_comen'] = self.limpiesa( comen.find('div', class_= 'cRVSd').text, 'p_fecha_comen')   if comen.find('div', class_= 'cRVSd') is not None else ''
                    incommet['p_puntuacion']= comen.find('span', class_= 'ui_bubble_rating').attrs['class'][1] if comen.find('span', class_= 'ui_bubble_rating') is not None else ''
                    incommet['p_puntuacion'] = self.limpiesa(incommet['p_puntuacion'],'burble' )
                    incommet['p_pais_de_origen'] = comen.find('span', class_= 'RdTWF').text if comen.find('span', class_= 'RdTWF') is not None else ''
                    incommet['p_n_contributions'] = float(comen.find('span', class_= 'yRNgz').text) if comen.find('span', class_= 'yRNgz') is not None else ''
                    incommet['p_date_stay'] = comen.find('span', class_= 'teHYY _R Me S4 H3').text if comen.find('span', class_= 'teHYY _R Me S4 H3') is not None else ''
                    
                    incommet['p_date_stay']= self.limpiesa(incommet['p_date_stay'][14:],'fecha' )   if incommet['p_date_stay'] != '' else ''
                    # teHYY _R Me S4 H3
                    hcomen = hcomen + [incommet]
                except:
                     pass
            return hcomen
        except:
            print('algo pasa con ' )
            pass

    def ingest(self,ciudad):
        resultado= []
        eq = self.hotelesc()
        for hotel in eq:
            try:
                h_registrado = {}
                h_registrado = self.inf_hotel( h_registrado, hotel)
                #self.open_hidenc()
                hcomen = self.get_comments( h_registrado['nombre_id'])
                if hcomen!=[]:
                    h_registrado['comentarios']= hcomen 
                else:
                    print("no hay cooemtarios en hotel")
                    h_registrado = {}
                resultado= resultado + [h_registrado]
            except:
                pass

            
        print('hola estoy aqui')
        
        json_object = json.dumps(resultado)
        with open("tripadvisor/" +ciudad +"-tripad.json", "w") as outfile:
            outfile.write(json_object)
        return resultado


if __name__ == "__main__":
    
    #ciudad= 'ambato'
    #sol= Hotel_Tripadvisor(ciudad).ingest(ciudad+ 'v2')
    sol= []
    ciudad= 'guayaquil'
    sol= Hotel_Tripadvisor(ciudad).ingest(ciudad+ 'v2')+ sol

    ciudad= 'quito'
    sol= Hotel_Tripadvisor(ciudad).ingest(ciudad+ 'v2')+ sol

    ciudad= 'manta'
    sol= Hotel_Tripadvisor(ciudad).ingest(ciudad+ 'v2')+ sol
    
    ciudad= 'ibarra'
    sol= Hotel_Tripadvisor(ciudad).ingest(ciudad+ 'v2')+ sol

    ciudad= 'loja'
    sol= Hotel_Tripadvisor(ciudad).ingest(ciudad+ 'v2')+ sol

    


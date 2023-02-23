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
            eq = soup.find('div',id="EATERY_SEARCH_RESULTS").find_all('div', class_= 'YHnoF Gi o')  ## encuantra la lista de hoteles que hay que  prw_rup prw_meta_hsx_responsive_listing ui_section listItem
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
            full_month_format = "%B %d %Y"
            full_month_date= value.replace(',', '')
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
            url_re = self.url + hotel.find('a',class_= 'Lwqic Cj b')['href']
            time.sleep(2)
            #h_registrado["descripccion"]=hotel.find('a',class_="review_count").text
            h_registrado["sitio_web"]=url_re
            ## ingresando al hotel
            time.sleep(1)
            self.driver.get(url_re)
            time.sleep(2)
           
            self.clickon('/html/body/div[11]/section/div/div/div[2]/div/div[1]/button')  # si existe el aununcio d etraducir
            self.scrooll()
            time.sleep(1)
            page = self.driver.page_source
            soup = BeautifulSoup(page, 'html.parser')  
            h_registrado['tipo'] = 'restaurante'
            h_registrado['fecha_view'] = dt.datetime.today().strftime('%Y-%m-%d')
            h_registrado['nombre_id'] = soup.find('h1',class_='HjBfq').text     if soup.find('h1',class_='HjBfq') is not None else ''
            

            h_registrado["direccion"] = soup.find('div',class_='kDZhm IdiaP Me').find('span', class_='yEWoV').text     if soup.find('div',class_='kDZhm IdiaP Me').find('span', class_='yEWoV') is not None else ''
                          # if soup.find('h1',class_="QdLfr b d Pn") is not None else ''
            h_registrado["puntuacion"]= float(soup.find('span',class_='ZDEqb').text[:3])  if soup.find('span',class_='ZDEqb') is not None else ''
            coment= [i.text for i in soup.find_all('div',class_='SrqKb')]
            h_registrado["descripcion"]= ",".join(coment)
          
            h_registrado["ciudad"]=self.ciudad
            
        

            time.sleep(0.5)
            self.clickon('/html/body/div[2]/div[2]/div[2]/div[6]/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[4]/div/div[2]/div[1]/div[1]/label/span')
            self.clickon('/html/body/div[2]/div[2]/div[2]/div[6]/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[4]/div/div[2]/div[1]/div[1]/label/span') if self.clickon('/html/body/div[2]/div[2]/div[2]/div[6]/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[4]/div/div[2]/div[1]/div[1]') !=True else None
            self.scrooll()
            time.sleep(1.5)
            
            
           
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

            comentarios = soup.find_all('div',class_="mobile-more")
            for comen in comentarios:
                try:
                    incommet = dict()
                    incommet['nombreh_id']= hnombre 
                    incommet['p_comentario'] = comen.find('p',class_="partial_entry").text  if comen.find('p',class_="partial_entry") is not None else ''
                    incommet['p_fecha_comen'] = self.limpiesa(comen.find('span',class_="ratingDate")['title'] , 'fecha')   if comen.find('span',class_="ratingDate") is not None else ''
                    incommet['p_puntuacion']= comen.find('span', class_= 'ui_bubble_rating').attrs['class'][1] if comen.find('span', class_= 'ui_bubble_rating') is not None else ''
                    incommet['p_puntuacion'] = self.limpiesa(incommet['p_puntuacion'],'burble' )
                    
                 
                   
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
        for restaurante in eq:
            try:
                h_registrado = {}
                h_registrado = self.inf_hotel( h_registrado, restaurante)
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
        with open("tripadvisor_restau/basejson/rest" +ciudad +"_tripad.json", "w") as outfile:
            outfile.write(json_object)
        return resultado


if __name__ == "__main__":
    
    ciudades = ['ambato']
    for ciudad in ciudades:
        Hotel_Tripadvisor(ciudad).ingest(ciudad+ 'v1')

 
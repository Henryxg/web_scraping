import json
import requests
from lxml import html
from collections import OrderedDict
import selenium
from selenium import webdriver
import time 

driver = webdriver.Chrome("./chromedriver")
url="https://www.expedia.com//"
urlprueba= "https://www.expedia.com/Hotel-Search?adults=2&d1=2022-10-19&d2=2022-10-20&destination=Quito%2C%20Pichincha%2C%20Ecuador&endDate=2022-10-20&latLong=-0.220299%2C-78.511714&regionId=3623&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2022-10-19&theme=&useRewards=false&userIntent="
driver.get(urlprueba)
time.sleep(2)
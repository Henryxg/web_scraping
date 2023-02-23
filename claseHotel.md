## Estructura del algoritmo de extracion

El modulo que permite realizar el web scraping esta compuesto de varios metodos que permiten la extracion, limpieza y carga de los datos.

class Hotel_Tripadvisor():
    def __init__(self, ciudad):
       
    

    def clickon(self, xxpad):
       
    
   
    def scrooll(self):
       
    

    def hotelesc(self ):  
     
    def limpiesa(self, value, tipo):
    


    def inf_hotel(self, h_registrado, hotel):
    
    def open_hidenc(self):
          

    def get_comments(self, hnombre):
      
      
    def ingest(self,ciudad):
       


if __name__ == "__main__":
    
    #ciudad= 'ambato'
    #sol= Hotel_Tripadvisor(ciudad).ingest(ciudad+ 'v2')
    ciudades = ['ambato']
    sol=[]
    for ciudad in ciudades:
        sol= sol + Hotel_Tripadvisor(ciudad).ingest(ciudad+ 'v3')


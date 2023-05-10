import pandas as pd
import json
class Exporter_booking():
    def __init__(self, versionn):
        self.versionn= versionn

    def topandas_one( self, name,all_coments):
        ruta= 'booking/basejson/'+name+'.json'
        df = pd.read_json(ruta)
        df.head()
        f = open(ruta)
        data = json.load(f)
        df['sitio_web']= df['link'] if 'link' in df.columns else df['sitio_web']
        base_one= df[['sitio_web', 'tipo', 'fecha_view', 'descripcion', 'nombre_id', 'precio',
       'direccion', 'puntuacion', 'calficacion_tx', 'ciudad', 'n_habitaciones']]
        
        for i in data:
            if 'comentarios' in i:
                all_coments= all_coments+i['comentarios'] 
            else:
                None
        

        return base_one, all_coments
    
    def tocsv(self, compania):
        
        nom_ciud= ["ambato"+self.versionn+"_"+ compania ,\
                    "quito"+self.versionn+"_"+ compania,\
                    "ibarra"+self.versionn+"_"+ compania,\
                    "manta"+self.versionn+"_"+ compania,\
                    "guayaquil"+self.versionn+"_"+ compania]

        base, coemntarios = self.topandas_one("loja"+self.versionn+"_"+ compania,[])
        
        for i in nom_ciud:
            valores= self.topandas_one(i,coemntarios)
            base=pd.concat([base ,valores[0] ])
            coemntarios =coemntarios + valores[1] 
        base= base[pd.notna(base['sitio_web'])]
        coemntarios= pd.DataFrame(coemntarios)
        coemntarios.to_csv('data/base_'+compania+'_comentarios.csv',index=False)
        base.to_csv('data/base_'+compania+'_hotel.csv',index=False)


Exporter_booking('v4').tocsv('booking')
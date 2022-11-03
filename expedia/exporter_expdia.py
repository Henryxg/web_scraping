import pandas as pd
import json
class Exporter_expedia():
    def __init__(self, versionn):
        self.versionn= versionn

    def topandas_one( self, name,all_coments):
        ruta= 'expedia/basejson/'+name+'.json'
        df = pd.read_json(ruta)
        df.head()
        f = open(ruta)
        data = json.load(f)

        base_one= df[['fecha_view', 'tipo', 'sitio_web', 'nombre_id', 'precio', 'puntuacion',
       'direccion', 'descripccion', 'ciudad', 'n_habitaciones']]
        
        for i in data:
            if 'comentarios' in i:
                all_coments= all_coments+i['comentarios'] 
            else:
                None
        

        return base_one, all_coments
    
    def tocsv(self, compania):
        
        nom_ciud= ["ambato"+self.versionn+"_expedia","quito"+self.versionn+"_expedia","ibarra"+self.versionn+"_expedia","manta"+self.versionn+"_expedia",\
            "guayaquill"+self.versionn+"_expedia"]

        base, coemntarios = self.topandas_one("loja"+self.versionn+"_expedia",[])
        
        for i in nom_ciud:
            valores= self.topandas_one(i,coemntarios)
            base=pd.concat([base ,valores[0] ])
            coemntarios =coemntarios + valores[1] 
        base= base[pd.notna(base['sitio_web'])]
        coemntarios= pd.DataFrame(coemntarios)
        coemntarios.to_csv('data/base_'+compania+'_comentarios.csv')
        base.to_csv('data/base_'+compania+'_hotel.csv')


Exporter_expedia('v2').tocsv('expedia')
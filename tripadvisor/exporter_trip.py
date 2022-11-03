import pandas as pd
import json
class Exporter_tripadvisor(versionn):
    def __init__(self, versionn):
        self.versionn= versionn

    def topandas_one( self, name,all_coments):
        df = pd.read_json('experdia/'+name+'.json')
        df.head()
        f = open('exedia/'+name+'.json')
        data = json.load(f)

        base_one= df[['link', 'tipo', 'fecha_view', 'nombre_id', 'precio', 'direccion',
            'puntuacion', 'descripcion', 'calficacion_tx', 'sitio_web', 'ciudad']]
        
        for i in data:
            if 'comentarios' in i:
                all_coments= all_coments+i['comentarios'] 
            else:
                None
        

        return base_one, all_coments
    
    def tocsv(self, compania):
        
        nom_ciud= ["loja-tripad","manta-tripad","quito-tripad"]

        base, coemntarios = self.topandas_one("ambato-tripad",[])
        
        for i in nom_ciud:
            valores= self.topandas_one(i,coemntarios)
            base=pd.concat([base ,valores[0] ])
            coemntarios =coemntarios + valores[1] 
        base= base[pd.notna(base['link'])]
        coemntarios= pd.DataFrame(coemntarios)
        coemntarios.to_csv('data/base_'+compania+'_comentarios.csv')
        base.to_csv('data/base_'+compania+'_hotel.csv')




import psycopg2
from psycopg2 import Error
import pandas as pd
import numpy as np
import json
import unicodedata
from psycopg2.extensions import AsIs
from sqlalchemy import create_engine

class Upfollowalerts:
    def __init__(self):
        


        self.conn_string = 'postgresql://postgres:JHEQWR2ZUASDasdgASd98x@155.138.253.162/indicadores_turismo'
        self.dba_connection='pgsql'
        self.dba_host='155.138.253.162'
        self.dba_port='5432'
        self.dba_name='indicadores_turismo'
        self.dba_passw = 'JHEQWR2ZUASDasdgASd98x'
        self.dba_user = 'postgres'
        
            
    def get_cursor(self, db_name, db_user ,db_passw , db_host, db_port ):
            conn = psycopg2.connect(
            user= db_user,
            password= db_passw,
            host= db_host,
            port= db_port,
            database=db_name
            )
            cur = conn.cursor()
            return cur, conn


    def get_id_columns(self, tablen, id , dba_name , dbb_user, dbb_passw, dbb_host, dbb_port ):
        try:
            cur, conn = self.get_cursor(dba_name, dbb_user ,dbb_passw , dbb_host, dbb_port  )
            cur.execute(f"SELECT {id} FROM {tablen} ;") # iden_nac_viv
            ids_db=cur.fetchall()        
            #conn.commit() ##Make the changes to the database persistent
            cur.execute(f"SELECT * FROM {tablen} LIMIT 1;")
            column_names = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()
            return [register[0] for register in ids_db], column_names

        except:
            print('conexion fallida')
    def updated_hotel(self, source_id):
        db = create_engine(self.conn_string)
        data_base= pd.read_csv('data/base_'+source_id+'_hotel.csv' )
        data_base = data_base
        iids, column = self.get_id_columns( 'hotel_name' , 'nombre_id' ,self.dba_name ,self.dba_user, self.dba_passw, self.dba_host, self.dba_port  )
        for i in column:
             data_base[i] =  data_base[i] if i in data_base.columns else None
        data_base['source_id']= source_id
       
        df_alll=data_base[['nombre_id',  'tipo', 'source_id','fecha_view', 'precio', 'direccion','puntuacion', 'descripcion', 'calficacion_tx', 'sitio_web', 'ciudad']]
        conn = db.connect()  
        df_alll.to_sql('hotel_name', conn, if_exists= 'append', index=False)

    def updated_comentario(self,source_id):
        db = create_engine(self.conn_string)
        data_base= pd.read_csv('data/base_'+source_id+'_comentarios.csv' )
        data_base = data_base
        #iids, column = self.get_id_columns( 'comentario_ho' , 'p_puntuacion' ,self.dba_name ,self.dba_user, self.dba_passw, self.dba_host, self.dba_port  )
        #for i in column:
         #   data_base[i]=data_base[i] if i in data_base.columns else None 
        df_alll=data_base[['nombreh_id', 'p_comentario', 'p_fecha_comen', 'p_puntuacion',
       'p_pais_de_origen', 'p_n_contributions', 'p_date_stay']]
        conn = db.connect()  
        df_alll.to_sql('comentario_ho', conn, if_exists= 'append', index=False)
           
Upfollowalerts().updated_comentario('tripadvisor')

           

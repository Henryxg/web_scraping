class Schemas:
    def __init__(self) -> None:
        self.schema= {
            'quito':        {
                'url': 'https://www.expedia.com/Hotel-Search?adults=2&d1=&d2=&destination=Quito%2C%20Pichincha%2C%20Ecuador&endDate=2022-11-03&latLong=-0.220299%2C-78.511714&regionId=3623&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2022-11-02&theme=&useRewards=true&userIntent=',
                'h_nombre': 'QdLfr b d Pn'

            },


            'guayaquil':    {

                'url' :''

            },

            'ambato':       {
                'url':''


            }, 

            'ibarra':       {
                'url': ''


            }, 

            'manta':        {

                'url':''

            }, 

            'loja':         {

                'url' : '',
                'h_nombre': 'biGQs _P fiohW eIegw'

            }, 

            'restosierra': {    



            },


            'restoamazonia': {


            },



            'restocosta': {


            },
            
        }
    def getSchema(self, schema_name):
        return self.schema[schema_name] if schema_name in self.schema else False
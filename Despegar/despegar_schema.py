class Schemas:
    def __init__(self) -> None:
        self.schema= {
            'quito':        {
                'url': 'https://www.despegar.com.ec/accommodations/results/CIT_7697/2022-10-27/2022-10-28/1?from=SB2&facet=city&searchId=41cbef7e-180e-465d-93cd-1d387d7f1a6c',
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
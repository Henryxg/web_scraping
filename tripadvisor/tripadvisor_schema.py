class Schemas:
    def __init__(self) -> None:
        self.schema= {
            'quito':        {
                'url': 'https://www.tripadvisor.es/Hotels-g294308-Quito_Pichincha_Province-Hotels.html',
                'h_nombre': 'QdLfr b d Pn'

            },


            'guayaquil':    {

                'url' :'https://www.tripadvisor.es/Hotels-g303845-a_ufe.true-Guayaquil_Guayas_Province-Hotels.html'

            },

            'ambato':       {
                'url':'https://www.tripadvisor.es/Hotels-g677335-Ambato_Tungurahua_Province-Hotels.html'


            },

            'ibarra':       {
                'url': 'https://www.tripadvisor.es/Hotels-g312858-Ibarra_Imbabura_Province-Hotels.html'


            },

            'manta':        {

                'url':'https://www.tripadvisor.es/Hotels-g297538-Manta_Manabi_Province-Hotels.html'

            },

            'loja':         {

                'url' : 'https://www.tripadvisor.es/Hotels-g644406-Loja_Loja_Province-Hotels.html',
                'h_nombre': 'biGQs _P fiohW eIegw'

            },

            'Esmeraldas': {   
                
                'url' : 'https://www.tripadvisor.com/Hotels-g612478-Esmeraldas_Esmeraldas_Province-Hotels.html', 

            },


            'restoamazonia': {


            },



            'restocosta': {


            },
            
        }
    def getSchema(self, schema_name):
        return self.schema[schema_name] if schema_name in self.schema else False
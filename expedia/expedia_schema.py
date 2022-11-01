class Schemas:
    def __init__(self) -> None:
        self.schema= {
            'quito':        {
                'url': 'https://www.expedia.com/Hotel-Search?adults=2&d1=&d2=&destination=Quito%2C%20Pichincha%2C%20Ecuador&endDate=2022-11-03&latLong=-0.220299%2C-78.511714&regionId=3623&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2022-11-02&theme=&useRewards=true&userIntent=',
                'h_nombre': 'QdLfr b d Pn'

            },


            'guayaquil':    {

                'url' :'https://www.expedia.com/Hotel-Search?adults=2&destination=Guayaquil%2C%20Guayaquil%2C%20Guayas%2C%20Ecuador&directFlights=false&endDate=2022-11-03&hotels-destination=Guayaquil&l10n=%5Bobject%20Object%5D&latLong=-2.171%2C-79.922359&localDateFormat=M%2Fd%2Fyyyy&partialStay=false&regionId=6337570&semdtl=&sort=RECOMMENDED&startDate=2022-11-02&theme=&useRewards=true&userIntent='

            },

            'ambato':       {
                'url':'https://www.expedia.com/Hotel-Search?adults=2&destination=Ambato%2C%20Tungurahua%2C%20Ecuador&directFlights=false&endDate=2022-11-03&hotels-destination=Ambato&l10n=%5Bobject%20Object%5D&latLong=-1.254344%2C-78.622842&localDateFormat=M%2Fd%2Fyyyy&partialStay=false&regionId=6150423&semdtl=&sort=RECOMMENDED&startDate=2022-11-02&theme=&useRewards=true&userIntent='


            }, 

            'ibarra':       {
                'url': 'https://www.expedia.com/Hotel-Search?adults=2&destination=Ibarra%2C%20Ibarra%2C%20Imbabura%2C%20Ecuador&directFlights=false&endDate=2022-11-03&hotels-destination=Ibarra&l10n=%5Bobject%20Object%5D&latLong=0.363453%2C-78.124128&localDateFormat=M%2Fd%2Fyyyy&partialStay=false&regionId=180439&semdtl=&sort=RECOMMENDED&startDate=2022-11-02&theme=&useRewards=true&userIntent='


            }, 

            'manta':        {

                'url':'https://www.expedia.com/Hotel-Search?adults=2&destination=Manta%2C%20Manta%2C%20Manabi%2C%20Ecuador&directFlights=false&endDate=2022-11-03&hotels-destination=manta&l10n=%5Bobject%20Object%5D&localDateFormat=M%2Fd%2Fyyyy&partialStay=false&regionId=6053676&semdtl=&sort=RECOMMENDED&startDate=2022-11-02&theme=&useRewards=true&userIntent='

            }, 

            'loja':         {

                'url' : 'https://www.expedia.com/Hotel-Search?adults=2&destination=Loja%2C%20Loja%2C%20Loja%20Province%2C%20Ecuador&directFlights=false&endDate=2022-11-03&hotels-destination=Loja&l10n=%5Bobject%20Object%5D&latLong=-3.998196%2C-79.202025&localDateFormat=M%2Fd%2Fyyyy&partialStay=false&regionId=2113&semdtl=&sort=RECOMMENDED&startDate=2022-11-02&theme=&useRewards=true&userIntent=',
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
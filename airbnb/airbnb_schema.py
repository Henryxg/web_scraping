class Schemas:
    def __init__(self) -> None:
        self.schema= {
            'quito':        {
                'url': 'https://www.airbnb.com/s/Quito--Pichincha--Ecuador/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=Quito%2C%20Pichincha&date_picker_type=calendar&place_id=ChIJn3xCAkCa1ZERclXvWOGRuUQ&flexible_date_search_filter_type=3&checkin=2022-10-28&checkout=2022-10-29&source=structured_search_input_header&search_type=autocomplete_click',
                'h_nombre': 'QdLfr b d Pn'

            },


            'guayaquil':    {

                'url' :'https://www.booking.com/searchresults.html?aid=378266&label=booking-name-IquAp%2AEbiLS6jPVl_he8yQS461499016255%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9069556%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YYriJK-Ikd_dLBPOo0BdMww&sid=dde0145e7f3a95c52398006b418ce0cf&checkin=2022-10-30&checkout=2022-10-31&city=-927505&group_adults=1&group_children=0&highlighted_hotels=4092846&hlrd=with_av&keep_landing=1&no_rooms=1&redirected=1&source=hotel&srpvid=7ee3982c5fb20272&room1=A,;#hotelTmpl'

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

            'restosierra': {    



            },


            'restoamazonia': {


            },



            'restocosta': {


            },
            
        }
    def getSchema(self, schema_name):
        return self.schema[schema_name] if schema_name in self.schema else False
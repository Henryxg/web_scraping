class Schemas:
    def __init__(self) -> None:
        self.schema= {
            'quito':        {
                'url': 'https://www.airbnb.com/s/Quito--Pichincha--Ecuador/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=Quito%2C%20Pichincha&date_picker_type=calendar&place_id=ChIJn3xCAkCa1ZERclXvWOGRuUQ&flexible_date_search_filter_type=3&checkin=2022-10-28&checkout=2022-10-29&source=structured_search_input_header&search_type=autocomplete_click',
                'h_nombre': 'QdLfr b d Pn'

            },


            'guayaquil':    {

                'url' :'https://www.airbnb.com.ec/s/Guayaquil--Guayas--Ecuador/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=Guayaquil%2C%20Guayas&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&place_id=ChIJX4BV6MsTLZARc6T89JKkFYA&checkin=2022-11-10&checkout=2022-11-11&_set_bev_on_new_domain=1671311638_NWY1NzA3YmZlZTNm'

            },

            'ambato':       {
                'url':'https://www.airbnb.com/s/Ambato--Tungurahua--Ecuador/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=1&query=Ambato%2C%20Tungurahua&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&checkin=2022-11-10&checkout=2022-11-11&place_id=ChIJH1Xvf6OB05ERGxYy2CS8LXo'


            },

            'ibarra':       {
                'url': 'https://www.airbnb.com/s/Ibarra--Imbabura--Ecuador/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=1&query=Ibarra%2C%20Imbabura&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&checkin=2022-11-10&checkout=2022-11-11&place_id=ChIJXTdbeKE8Ko4R22oFPhM_cIU'


            },

            'manta':        {

                'url':'https://www.airbnb.com/s/Manta--Manab%C3%AD--Ecuador/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=1&query=Manta%2C%20Manab%C3%AD&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&checkin=2022-11-10&checkout=2022-11-11&place_id=ChIJi5hA5KnmK5ARuphvqSW4A5Q'

            },

            'loja':         {

                'url' : 'https://www.airbnb.com/s/Loja--Ecuador/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=1&query=Loja%2C%20Ecuador&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&checkin=2022-11-10&checkout=2022-11-11&place_id=ChIJLR25YQZIy5ERCe4e3HwTEo4',
                'h_nombre': 'biGQs _P fiohW eIegw'

            },
            'baños': {
                'url' : 'https://www.airbnb.com/s/Ambato--Ba%C3%B1os-de-Agua-Santa--Ecuador/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=Ambato%2C%20Ba%C3%B1os%20de%20Agua%20Santa&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click&place_id=EiVBbWJhdG8sIEJhw7FvcyBkZSBBZ3VhIFNhbnRhLCBFY3VhZG9yIi4qLAoUChIJX15wKyKR05ERH5F9AEtXB2oSFAoSCYkmCGAikdOREemu2PzyyGfb&checkin=2023-03-21&checkout=2023-03-22',


            },

            'esmeraldas': {    

                'url': 'https://www.airbnb.com/s/Esmeraldas--Ecuador/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-06-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&query=Esmeraldas%2C%20Ecuador&date_picker_type=calendar&place_id=ChIJo4gQ2boxK44RLocNouWCiiQ&checkin=2023-05-10&checkout=2023-05-12&source=structured_search_input_header&search_type=autocomplete_click'

            },


            'restoamazonia': {


            },



            'restocosta': {


            },

            
        }
    def getSchema(self, schema_name):
        return self.schema[schema_name] if schema_name in self.schema else False
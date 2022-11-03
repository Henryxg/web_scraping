class Schemas:
    def __init__(self) -> None:
        self.schema= {
            'quito':        {
                'url': 'https://www.booking.com/searchresults.html?ss=Quito&ssne=Quito&ssne_untouched=Quito&label=gen173nr-1FCAQoggJCDHNlYXJjaF9xdWl0b0gzWARoQYgBAZgBMbgBGcgBDNgBAegBAfgBA4gCAagCA7gC_pfdmgbAAgHSAiQ4YjFmZjkxZS1mNDA0LTQ2ODMtOTRhNC03NTZmMWIxOGI3YjLYAgXgAgE&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-932573&dest_type=city&checkin=2022-10-27&checkout=2022-10-28&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure',
                'h_nombre': 'QdLfr b d Pn'

            },


            'guayaquil':    {

                'url' :'https://www.booking.com/searchresults.html?aid=378266&label=booking-name-IquAp%2AEbiLS6jPVl_he8yQS461499016255%3Apl%3Ata%3Ap1%3Ap22%2C563%2C000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9069556%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YYriJK-Ikd_dLBPOo0BdMww&sid=dde0145e7f3a95c52398006b418ce0cf&checkin=2022-10-30&checkout=2022-10-31&city=-927505&group_adults=1&group_children=0&highlighted_hotels=4092846&hlrd=with_av&keep_landing=1&no_rooms=1&redirected=1&source=hotel&srpvid=7ee3982c5fb20272&room1=A,;#hotelTmpl'

            },

            'ambato':       {
                'url':'https://www.booking.com/searchresults.en-us.html?ss=Ambato&ssne=Quito&ssne_untouched=Quito&label=gen173nr-1FCAQoggJCDHNlYXJjaF9xdWl0b0gzWARoQYgBAZgBMbgBGcgBDNgBAegBAfgBA4gCAagCA7gC_pfdmgbAAgHSAiQ4YjFmZjkxZS1mNDA0LTQ2ODMtOTRhNC03NTZmMWIxOGI3YjLYAgXgAgE&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-924303&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=deb578739559002a&ac_meta=GhBkZWI1Nzg3Mzk1NTkwMDJhIAAoATICZW46BkFtYmF0b0AASgBQAA%3D%3D&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'


            },

            'ibarra':       {
                'url': 'https://www.booking.com/searchresults.en-us.html?ss=Ibarra%2C+Imbabura%2C+Ecuador&ssne=Ibarra&ssne_untouched=Ibarra&label=gen173nr-1FCAQoggJCDHNlYXJjaF9xdWl0b0gzWARoQYgBAZgBMbgBGcgBDNgBAegBAfgBA4gCAagCA7gC_pfdmgbAAgHSAiQ4YjFmZjkxZS1mNDA0LTQ2ODMtOTRhNC03NTZmMWIxOGI3YjLYAgXgAgE&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-929344&dest_type=city&ac_position=0&ac_click_type=b&ac_langcode=en&ac_suggestion_list_length=5&search_selected=true&search_pageview_id=4f23788e2bb70059&ac_meta=GhA0ZjIzNzg4ZTJiYjcwMDU5IAAoATICZW46BkliYXJyYUAASgBQAA%3D%3D&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'


            },

            'manta':        {

                'url':'https://www.booking.com/searchresults.en-us.html?ss=Manta&ssne=Manta&ssne_untouched=Manta&label=gen173nr-1FCAQoggJCDHNlYXJjaF9xdWl0b0gzWARoQYgBAZgBMbgBGcgBDNgBAegBAfgBA4gCAagCA7gC_pfdmgbAAgHSAiQ4YjFmZjkxZS1mNDA0LTQ2ODMtOTRhNC03NTZmMWIxOGI3YjLYAgXgAgE&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-930612&dest_type=city&checkin=2022-11-10&checkout=2022-11-11&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure'

            },

            'loja':         {

                'url' : 'https://www.booking.com/searchresults.en-us.html?ss=Loja&ssne=Loja&ssne_untouched=Loja&label=gen173nr-1FCAQoggJCDHNlYXJjaF9xdWl0b0gzWARoQYgBAZgBMbgBGcgBDNgBAegBAfgBA4gCAagCA7gC_pfdmgbAAgHSAiQ4YjFmZjkxZS1mNDA0LTQ2ODMtOTRhNC03NTZmMWIxOGI3YjLYAgXgAgE&aid=304142&lang=en-us&sb=1&src_elem=sb&src=searchresults&dest_id=-930353&dest_type=city&checkin=2022-11-10&checkout=2022-11-11&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure',
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
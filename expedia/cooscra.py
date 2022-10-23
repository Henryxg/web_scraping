

from playwright.sync_api import sync_playwright
import requests


def get_cookie_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch() 
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.expedia.com///Quito-Hotels-Casa-Gangotena.h6793417.Hotel-Information?chkin=2022-10-19&chkout=2022-10-20&x_pwa=1&rfrr=HSR&pwa_ts=1665260836841&referrerUrl=aHR0cHM6Ly93d3cuZXhwZWRpYS5jb20vSG90ZWwtU2VhcmNo&useRewards=false&rm1=a2&regionId=3623&destination=Quito%2C+Pichincha%2C+Ecuador&destType=MARKET&neighborhoodId=553248635976396551&trackingData=AAAAELYkqUPj0RCvea8L5oezJ1ttvqrsIsdmtBPfGBDsPemOoQB3HbSwHHxoJLIzlMmUCDmLEuXiFH7aDlLlebh_l4KOmYj0m-fvlO8XcsoG80_kAoWofzHvRJJ9RBTrPjL0Zh-QY-m7jtOM9MQYJjahDr5bNr-imwG-0vknQqSI5I7bBSfR8aHV0IoELmOaqiuCxDxyTfvFTn3WpPmlRtJnoF6PTKAOdGNUyvKAJzfLGLg8UBxt518GDq8BybhSWHejBI0-fBLzgz5C6Kg2EYjD5hVF9JaZH-oqYmlyNR6et3B5GGHpmV2Lj83jSf9Oj7tGe06ui9GQZyX0P6qLapeth0r4azfySkvxXnXQUJcmbHf0xzg99z8vIUEVxshzjbMBcEHyaoBB1IGpLxZ3H3fNJZWJI16yVtUzT4_hQSGvgi4BX-6lXCJeh7xOPF9zXsfq5UU3R46wZBYW00vAfVKx-yspldgOHG496NjxiuB81Lo6qCtVH8sdwH9bovEGT49Fy8MuTVN5JXl-tzANKyy2GJhR5CehonGl-ArDp-PrhhACdPqZJLQvxnULNT1KuAi-OQhDAS1CDPI-xXPjL3Vj0fNoiX4YDIuagsM6ssWGKXtV0lz4wzNFLJwnU8KhzU4yrrqLSux1FaYNhriJl5Yj5GYy8fq0pMMj-moxYVdKhU-5g7gd7jW4kYhaoNxH0YN6Ngr98rJC6H24A5gtfU84GbL-XP1333EHCdpyVRVYmWmxnY_cjUaexthWrxlm3D6ySoCIpMWzPeDQi2JY2_OAWJGT90AmQNCu7-cz-4NSA6AnfcMAHTK5EmigqMdH8TXU46Jl5dkRRGDijpY3RikmNmSJ39lFCuzRJPU9o0dOACN7b6UbzJ5p5k8tI2MTefKiKt2GAbEhESvvc1yWVxk2cl8q92kxVxJoLjZ4rf0uBRVSV7wQLEDjN8tvMASROb6TTeWX74xtYx7d9NSR8s7RiCNQbFsQnn54uWiI_G9sFhfRhMcIiUK0ynzejwrQNV0PVKrLHHt0kD-IgxCBxbxXKZXwuDsMYaBWaJltOcaxP54mT_rvX4jsWN1Hk1ohc86lG7tOZXl2w4I9lERDqDAOKVGUilXJJWnQnJNEwyjrG8eVra8zbLb7u9Yr9OQOEqAf4w%3D%3D&rank=1&testVersionOverride=Buttercup%2C44204.0.0%2C44203.0.0%2C43549.129874.3%2C43550.131256.0%2C31936.102311.0%2C33775.98848.1%2C38414.114301.0%2C39483.0.0%2C38427.115718.1%2C42444.0.0%2C42589.0.0%2C42876.124673.0%2C42973.0.0%2C42974.0.0%2C42975.0.0%2C42976.0.0%2C42802.125960.1%2C33739.99567.0%2C37898.109354.1%2C37930.0.0%2C37949.0.0%2C37354.113955.1%2C43435.128144.0%2C43153.132057.0%2C44700.0.0%2C44704.0.0&slots=&position=1&beaconIssued=2022-10-08T20%3A27%3A15&sort=RECOMMENDED&top_dp=331&top_cur=USD&semdtl=&userIntent=&selectedRoomType=214202092&selectedRatePlan=248034741")
        page.click('Reviews')
        page.click('Reviews')
        page.click('Reviews')
        page1.getByRole('link', { name: 'Reviews' }).click()
        cookie_for_requests = context.cookies()[3]['value']
        #page.click("button.trustarc-agree-btn")
        # print(context.cookies())
        cookie_for_requests = context.cookies()[3]['value']
        browser.close()
    return cookie_for_requests


def req_with_cookie(cookie_for_requests):
    cookies = dict(
        Cookie=f'notice_preferences=2:; notice_gdpr_prefs=0,1,2::implied,eu; euconsent-v2={cookie_for_requests};')
    r = requests.get("https://www.forbes.com/billionaires/page-data/index/page-data.json", cookies=cookies)
    return r.json()


if __name__ == '__main__':
    data = req_with_cookie(get_cookie_playwright())
    print(data['result']['pageContext']['tableData'][0])
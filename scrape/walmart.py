import requests
from bs4 import BeautifulSoup as bs
import json
from pathlib import Path
import pandas as pd
from collections import defaultdict

class WalmartClawler:
    
    def __init__(self):
    
        self.cookies_ = {
            'ak_bmsc': 'A48EF860330CEE7359ED031CB3FB6698~000000000000000000000000000000~YAAQRQosFzP2N96TAQAAAI0y+RrA4WtWGAwwOC1ggsD0PnnV0lA9fQlLcuvZk5vjWeGxzrwmOi/mv7CR9W0zJtJjCA5bdsGsIqhAcGV/F6fZ9BGtQr4NtKTwXvbujmnKxJg4lTtjcS1sQK/4tH635AOPrDKs3HMrR7FZNLJe8LZlG2SnGP94LinpegdVlC/gMdN0kQQpWJeMTpP/s1mihO3scWlFpanMI92F+L6ezb66oNyNCJWYIRnWz8I4d2NzZKaLvRCxRbz0chRLXsqdz/CQbMv1VT9bEybZA895NjtsHxb/VifHnxPMkxHKGZd6nnRQkKGRIw28HRN1p4Z2rv59GoibQe78oMTAn6TvcHehRJ1aHoVq7vP0EIcqWlm3wuoYil8AQXGBOaT7',
            '_astc': 'c8a8a2e7ff1c435414a63f052e4a9abb',
            'adblocked': 'true',
            'io_id': '4b9b6830-3ca7-4900-84f8-550e37bae91c',
            'ACID': '85eb8f84-53e8-48ad-bb07-78c3c44efc25',
            '_m': '9',
            'auth': 'MTAyOTYyMDE4HPKaHPLDgLiGwzrTFUXS1EJ6FK87Mkr9ute13UhD42q%2Fhs6fb8owbjcnavm1TJQfUFBb2mO9nm0BswYFY46Gzuhm09JdoHuVEaIKsQzBHo45SmLpppYzb1m8Yd2B4%2BEU767wuZloTfhm7Wk2KcjygsAEeU%2BeKCMhfP9XV060SY9YLFbnriK2ZO0kH8KTMx5ewf8gVT2FOkij9CEIYBsRgjVhiaWTpfEsLwxAa9DxkJAUMk70P8glgOEpLOprhDfMJ0tmvH1FCaN9tZDh4SCrHbZrd8o14HEAFb0qpKRxJOzkgcyMcFjrJlNmxiMcECGFN5W4RC8aj3rTioxjytqUlFK%2B0e4bSSZAi7mx4XNxiKLTyTtl2yaisCsejZtl%2Ft97qqHSn7ERTuo0ozrXeanPGLU3jWmD0ztc0AsUNRUx2N4%3D',
            'hasACID': 'true',
            'sod': 'torbit1735052660',
            'abqme': 'true',
            'vtc': 'fvufmeGXP6vL69HcFa_WRA',
            'bstc': 'fvufmeGXP6vL69HcFa_WRA',
            'mobileweb': '0',
            'xpth': 'x-o-mart%2BB2C~x-o-mverified%2Bfalse',
            'xpa': '9TmFO|KJ1PA|OIg9i|OQe8n|PA6e6|PDL7h|fdm-7|owcqA',
            'exp-ck': '9TmFO3KJ1PA2OIg9i1OQe8n2fdm-71',
            '_pxhd': 'e8ce12c9a9e5a39eec25b3ac5be025b5141cbd5b0deed103d6e964c03d4faee1:5a876c7e-c208-11ef-980b-959b66905f2d',
            '_intlbu': 'false',
            '_shcc': 'US',
            'assortmentStoreId': '3081',
            'hasLocData': '1',
            'locDataV3': 'eyJpc0RlZmF1bHRlZCI6dHJ1ZSwiaXNFeHBsaWNpdCI6ZmFsc2UsImludGVudCI6IlNISVBQSU5HIiwicGlja3VwIjpbeyJub2RlSWQiOiIzMDgxIiwiZGlzcGxheU5hbWUiOiJTYWNyYW1lbnRvIFN1cGVyY2VudGVyIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiOTU4MjkiLCJhZGRyZXNzTGluZTEiOiI4OTE1IEdFUkJFUiBST0FEIiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozOC40ODI2NzcsImxvbmdpdHVkZSI6LTEyMS4zNjkwMjZ9LCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInN0b3JlSHJzIjoiMDY6MDAtMjM6MDAiLCJhbGxvd2VkV0lDQWdlbmNpZXMiOlsiQ0EiXSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiUElDS1VQX1NQRUNJQUxfRVZFTlQiLCJQSUNLVVBfSU5TVE9SRSIsIlBJQ0tVUF9DVVJCU0lERSJdLCJ0aW1lWm9uZSI6IlBTVCIsInN0b3JlQnJhbmRGb3JtYXQiOiJXYWxtYXJ0IFN1cGVyY2VudGVyIiwic2VsZWN0aW9uVHlwZSI6IkRFRkFVTFRFRCJ9XSwic2hpcHBpbmdBZGRyZXNzIjp7ImxhdGl0dWRlIjozOC40ODI2NzcsImxvbmdpdHVkZSI6LTEyMS4zNjkwMjYsInBvc3RhbENvZGUiOiI5NTgyOSIsImNpdHkiOiJTYWNyYW1lbnRvIiwic3RhdGUiOiJDQSIsImNvdW50cnlDb2RlIjoiVVMiLCJsb2NhdGlvbkFjY3VyYWN5IjoibG93IiwiZ2lmdEFkZHJlc3MiOmZhbHNlLCJhbGxvd2VkV0lDQWdlbmNpZXMiOlsiQ0EiXX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMzA4MSIsImRpc3BsYXlOYW1lIjoiU2FjcmFtZW50byBTdXBlcmNlbnRlciIsImludGVudCI6IlBJQ0tVUCJ9LCJpbnN0b3JlIjpmYWxzZSwiZGVsaXZlcnkiOnsibm9kZUlkIjoiMzA4MSIsImRpc3BsYXlOYW1lIjoiU2FjcmFtZW50byBTdXBlcmNlbnRlciIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6Ijk1ODI5IiwiYWRkcmVzc0xpbmUxIjoiODkxNSBHRVJCRVIgUk9BRCIsImNpdHkiOiJTYWNyYW1lbnRvIiwic3RhdGUiOiJDQSIsImNvdW50cnkiOiJVUyJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6MzguNDgyNjc3LCJsb25naXR1ZGUiOi0xMjEuMzY5MDI2fSwic2NoZWR1bGVkRW5hYmxlZCI6ZmFsc2UsInVuU2NoZWR1bGVkRW5hYmxlZCI6ZmFsc2UsImFjY2Vzc1BvaW50cyI6W3siYWNjZXNzVHlwZSI6IkRFTElWRVJZX0FERFJFU1MifV0sImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsImFsbG93ZWRXSUNBZ2VuY2llcyI6WyJDQSJdLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJERUxJVkVSWV9BRERSRVNTIl0sInRpbWVab25lIjoiUFNUIiwic3RvcmVCcmFuZEZvcm1hdCI6IldhbG1hcnQgU3VwZXJjZW50ZXIiLCJzZWxlY3Rpb25UeXBlIjoiREVGQVVMVEVEIn0sImlzZ2VvSW50bFVzZXIiOmZhbHNlLCJtcERlbFN0b3JlQ291bnQiOjAsInJlZnJlc2hBdCI6MTczNTA3NDI2MjQ3NiwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOjg1ZWI4Zjg0LTUzZTgtNDhhZC1iYjA3LTc4YzNjNDRlZmMyNSJ9',
            'locGuestData': 'eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjp0cnVlLCJwaWNrdXAiOnsibm9kZUlkIjoiMzA4MSIsInRpbWVzdGFtcCI6MTczNTA1MjY2MjQ3Mywic2VsZWN0aW9uVHlwZSI6IkRFRkFVTFRFRCJ9LCJzaGlwcGluZ0FkZHJlc3MiOnsidGltZXN0YW1wIjoxNzM1MDUyNjYyNDczLCJ0eXBlIjoicGFydGlhbC1sb2NhdGlvbiIsImdpZnRBZGRyZXNzIjpmYWxzZSwicG9zdGFsQ29kZSI6Ijk1ODI5IiwiZGVsaXZlcnlTdG9yZUxpc3QiOlt7Im5vZGVJZCI6IjMwODEiLCJ0eXBlIjoiREVMSVZFUlkiLCJ0aW1lc3RhbXAiOjE3MzUwNTI2NjI0NjgsImRlbGl2ZXJ5VGllciI6bnVsbCwic2VsZWN0aW9uVHlwZSI6IkRFRkFVTFRFRCIsInNlbGVjdGlvblNvdXJjZSI6bnVsbH1dLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EifSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE3MzUwNTI2NjI0NzMsImJhc2UiOiI5NTgyOSJ9LCJtcCI6W10sIm1zcCI6eyJub2RlSWRzIjpbXSwidGltZXN0YW1wIjpudWxsfSwibXBEZWxTdG9yZUNvdW50IjowLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6ODVlYjhmODQtNTNlOC00OGFkLWJiMDctNzhjM2M0NGVmYzI1In0%3D',
            'xpm': '1%2B1735052664%2BfvufmeGXP6vL69HcFa_WRA~%2B0',
            'isCBBSession': 'true',
            'bm_mi': 'F54881461518CA01FCBBE7AED85CBBD8~YAAQRQosF+P7N96TAQAAgwAz+Rqliwi0oC7gjKeHRNQ7aAiqXpPYNXQBkexxasgoQ3AaL/x6NPEk6QWqlT4IBqytcxv9gRrfWkfKffGE0sxbHym7WGEhwfo4nlmShT92P2+S7hcb6FwnYN7lD+7a6YdC5oGxs5lfxSeu8t023qrMoKZcqlto2FPgvVKImyLpow/nH37MpdYNet37cLTC871OwB5ahY3Ctnfqi9uEP1giR/z6HLD7W9cx4670baz/kDAJW6GEmAlJMpbOezBYBJvN4IqTIdAdLDemDhxf0P/QflCaSGSRgLBH4nbFaoZpl5FDLdJccrGsvekUdDTN807iniF1kmuDPTWNnGsmEzmh5LXI2gwP5hG+R23o8fGRbpbwrQWL~1',
            'xptwj': 'uz:1ab4d8ac8932f741e0d9:8zacMSrLX9GQm/rat6IBeld1tqVexmm81vyWNBQWHLKQB6O2Xlrj/ClgpmyBmcigPWzZBFnDMrY8baT+EdZdSWpgAdYYUR6s4kc26XMF8iThVc8aX1pkc/KHuWvCEmQGT3wt0y+xre4e5nRN+ApUxJZokTxwaCbrBFQvU3c=',
            'xptc': '_m%2B9~assortmentStoreId%2B3081',
            'xptwg': '4211380496:2673D5BBCE50F60:5F2F87C:28E9AF7F:3F21E21A:D3B52E5A:',
            'TS012768cf': '01bab6ef38e6ad797e029f96e5ffa7ec5593f6c1c380878d8853b949ccb157834d62bb048b39e1f52c361263a23258d7c99f9e90d5',
            'TS01a90220': '01bab6ef38e6ad797e029f96e5ffa7ec5593f6c1c380878d8853b949ccb157834d62bb048b39e1f52c361263a23258d7c99f9e90d5',
            'TS2a5e0c5c027': '0826a4e0adab20007ceaef538e3fba65e912f32bf0c349300308ccc1353751021d1b90119e25f2c20855e78311113000ff496c7e3287a5f016bc4ea307409ec5fa51d8ee59400a91d8ea5d9843c0b0f319237e71d5517bce76bbf31172f065ce',
            'akavpau_p2': '1735053290~id=c14079c311a889225950aacfae71f507',
            'if_id': 'FMEZARSFcsFC8tKHfE9Sa311aftMBTDqRjnzFWfh1r93in4xDSqPHPC8puugYCYV514CfwOXG1+KAfaRQsO381erCXmC8oKeczhUklPybH8918tQaxMmutRl4tBmMAGUIwSJdgpk31oVkR42kwzeQVPWg4Sw6jcnW4GxLqlnMGK5RQafAdnw9V2tXoF7x2iCDmGDuwO32GDN5oWLLKSqEXMZdPqlwDXgGU4XgCjZfVYt/rLX32TBOUUBv508uAfm7PheCp86WXz5r45QG3beSA==',
            'TS016ef4c8': '0130689383f08310d1a69fcc539b7ba0c3e0b5aa60005795f77ee2c9a0c053880f63f2d241ab80c1864ac6df37b73fed00f316c8e4',
            'TS01f89308': '0130689383f08310d1a69fcc539b7ba0c3e0b5aa60005795f77ee2c9a0c053880f63f2d241ab80c1864ac6df37b73fed00f316c8e4',
            'TS8cb5a80e027': '08a31aaa44ab20004c62907764dfdfd9790cd34507afc617c8f4d575f9d060329fddd38597daff9408ab56472c113000a4121321c7b7dc508fbd990b9ec0e0ff6d0266623088f0fd886576da8b3371eb9772ec9d36d097c993f28b5ca0743cae',
            'bm_sv': '39DB50C01EFC5988A4B7043722B4519C~YAAQRQosFxQTON6TAQAAumY0+RrwDGvNNKEsxHuSACJpMonY3BM84S9mOkoXE/KRDMsz0ed2AHs7K09zjOdOdTsBbTk8A8+cJlVktfjk5DDJviNUx8iZdpxnQuLvVuO1MCZGlwZgl78P0YSkUIzDI75dOUE/cLC5p8vPrFztqpVs9WH5UzjfXf70x9I9hyF/UHdvb0shPuckRNtaa4yiq1oprVlbLpsnqYiQttsF+pXW84EwT9gpeP3ALmrJaoN9zw==~1',
        }

        self.headers_ = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.7',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'referer': 'https://www.google.com/',
            'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'sec-gpc': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        self.params_ = {
            'classType': 'REGULAR',
        }


    def send_data_request(self, url):
        self.url_status = []
        self.url = url
        try:
            response = requests.get(
                self.url,
                params=self.params_,
                cookies=self.cookies_,
                headers=self.headers_,
            )
            self.url_status.append([self.url,response.status_code])
            return response.text, response.status_code
        except requests.exceptions.RequestException as e:
            return [],e


    def get_data(self,url):
        self.raw_data, self.status = self.send_data_request(url)
        if self.status == 200:
            soup = bs(self.raw_data, 'html.parser')
            json_data = soup.find('script', id='__NEXT_DATA__', type="application/json")
            self.parsed_data = json.loads(json_data.text)
            self.product_page_data = self.parsed_data['props']['pageProps']['initialData']['data']['product']
            self.product_page_specs = self.parsed_data['props']['pageProps']['initialData']['data']['idml']
            self.product_page_review = self.parsed_data['props']['pageProps']['initialData']['data']['reviews']
            
            self.temp_dict = {}
            # SKU parsing
            try:
                sku = self.product_page_data['name']
            except KeyError:
                sku = pd.NA
            
            self.temp_dict["SKU"] = [sku]
            
            # Brand parsing
            try:
                brand = self.product_page_data['brand']
            except KeyError:
                brand = pd.NA
            
            self.temp_dict["Brand"]= [brand]
            
            # rating parsing
            try:
                rating  = self.product_page_data['averageRating']
            except KeyError:
                rating = pd.NA    
            
            self.temp_dict['Product Rating'] = [rating]
            
            # count parsing
            try:
                r_count = self.product_page_data['numberOfReviews']
            except KeyError:
                r_count = pd.NA
            
            self.temp_dict['Number of Reviews'] = [r_count]
            
            # upc parsing
            
            try:
                upc = self.product_page_data['upc']
            except KeyError:
                upc = pd.NA
            
            self.temp_dict['UPC'] = [upc]
            
            # upc id
            
            try:
                self.id_ = self.product_page_data['id']
            except KeyError:
                self.id_ = pd.NA
            
            self.temp_dict['Id'] = [self.id_]
            
            
            # product specs parsing
            try:
                specs = self.product_page_specs['specifications']
                for spec in specs:
                    self.temp_dict[spec['name']]= [spec['value']]
            except KeyError:
                None        
            
            # root
            self.temp_dict['root']=[self.url]
            
        else:
            print(f'{self.url} not parsed since the link is {self.status}')
            
            
    def write_file(self, data):
        product_file_path = Path.cwd() / 'python/scrape/product.csv'
        
        new_df = pd.DataFrame(data)
        
        if product_file_path.exists():
            existing_df = pd.read_csv(product_file_path)
            combined_df = pd.concat([new_df, existing_df], ignore_index=False)
        else:
            combined_df = new_df
        
        combined_df.to_csv(product_file_path, index=False)
        self.temp_dict.clear()
        


crawler1 = WalmartClawler()
link_list = [
    'https://www.walmart.com/ip/Meow-Mix-Original-Choice-Dry-Cat-Food-3-15-Pound-Bag/20435420',
    'https://www.walmart.com/ip/Sabrina-Carpenter-Cherry-Pop-EDP-30ml-1oz/5492571361?classType=REGULAR',
    'https://www.walmart.com/ip/Juicy-Couture-OUI-Play-Sparkling-Rebel-Eau-De-Parfum-Perfume-for-Women-0-5-oz/990327490?athcpid=990327490&athpgid=AthenaItempage&athcgid=null&athznid=si&athieid=v0_eeMjY2Ljc1LDM1ODc5LjQ0LDAuMDA3MDMzNjIzNDUxNzc0MjgxLDAuNV8&athstid=CS055~CS004&athguid=m-jcveGQAs8Gv-sNuXWO-_mEiaePzMeWWmEg&athancid=5492571361&athposb=0&athena=true&athbdg=L1600'
]

for link in link_list:
    crawler1.get_data(link)
    crawler1.write_file(crawler1.temp_dict)

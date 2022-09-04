import json
import sys
# import get_json_from_booli_id.py
# import get_booli_ids_from_url.py
# from get_booli_ids_from_url import *
from get_json_from_property_url import *
from get_property_urls_from_page_url import *

def get_page_urls_from_url(url, number_of_pages):
    # https://www.booli.se/slutpriser/orgryte/115321?objectType=Lägenhet&page=2
    urls = []
    urls.append(url)
    for i in range(2, number_of_pages+1):
        new_url = url + "&page=" + str(i)
        urls.append(new_url)
    return urls

if __name__ == "__main__":

    initial_url = sys.argv[1]
    number_of_pages = int(sys.argv[2])
    # booli_ids = get_booli_ids_from_url(initial_url, number_of_pages)
    page_urls = get_page_urls_from_url(initial_url, number_of_pages)

    for page_url in page_urls:
        print(page_url)

        # booli_ids = get_booli_ids_from_url(page_url)
        property_urls = get_property_urls_from_page_url(page_url)

        for property_url in property_urls:
            print(property_url)
            # json_property = get_json_from_booli_id(booli_id)
            property_json = get_json_from_property_url(property_url)
            file_name = property_url.split('booli.se/')[-1]
            file_name = file_name.replace('/','-')
            with open(file_name + ".json", 'w') as f:
                json.dump(property_json, f, indent=4)

#Probblems:
#1. boolId is not always reliable for looking up

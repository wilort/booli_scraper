import sys
import requests
import json
from bs4 import BeautifulSoup

def get_property_urls_from_json(json_dict):
    json_dict = json_dict['ROOT_QUERY']
    property_urls = []
    for key in json_dict.keys():
        if key.startswith("searchSold"):
            result_dict = json_dict[key]['result']
            break

    for x in result_dict:
        property_url = "https://www.booli.se" + x['url']
        property_urls.append(property_url)

    return property_urls

def get_property_urls_from_page_url(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Find the json string we are looking for
    script_elements = soup.find_all('script')
    for script_element in script_elements:
        if script_element.text.startswith('window.__APOLLO_STATE__'):
            json_string = script_element.text.split('= ',1)[1]
            break

    json_object = json.loads(json_string)

    property_urls = get_property_urls_from_json(json_object)
    return property_urls



if __name__ == "__main__":

    property_urls = get_property_urls_from_url(sys.argv[1])
    print('\n'.join(property_urls))

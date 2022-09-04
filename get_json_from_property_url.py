import requests
import json
import sys
from bs4 import BeautifulSoup

def get_property_json_from_json_dict(json_dict):
    json_dict = json_dict['ROOT_QUERY']
    for key in json_dict.keys():
        # If the json dict comes from e.g.
        # https://www.booli.se/annons/4456930
        if key.startswith("propertyByListingId"):
            return json_dict[key]
        # If the json dict comes from e.g.
        # https://www.booli.se/bostad/525471
        elif key.startswith("propertyByResidenceId"):
            return json_dict[key]

def get_json_from_property_url(url):

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Find the json string we are looking for
    # in the html code
    script_elements = soup.find_all('script')
    for script_element in script_elements:
        if script_element.text.startswith('window.__APOLLO_STATE__'):
            json_string = script_element.text.split('= ',1)[1]
            break

    json_object = json.loads(json_string)

    property_json = get_property_json_from_json_dict(json_object)
    return property_json


if __name__ == "__main__":

    property_json = get_json_from_property_url(sys.argv[1])
    # tmp = json.dumps(json_object, indent=4)
    property_json_formated = json.dumps(property_json, indent=4)
    print(property_json_formated)
    # get_json_from_booli_id("4714072")

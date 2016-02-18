
import nene
import requests
import os
import simplejson as json


EXISTING_ENDPOINTS_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'nene', 'endpoints.json')


def load_endpoint_json(path):
    """
    Loads a given JSON file & returns it.
    :param path: The path to the JSON file
    :type path: string
    :returns: The loaded data
    """
    with open(path, 'r') as endpoints_file:
        return json.load(endpoints_file)





def connect_purge():
    endpoints = load_endpoint_json(EXISTING_ENDPOINTS_FILE)
    return endpoints


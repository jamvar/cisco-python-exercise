import os
import re
import json
import requests

ip_address = raw_input("Enter ip_address in question:")

with open('{0}/parameters.json'.format(os.getcwd()), 'r') as f:
    parameters = f.read()
    if re.search(r'"<.*>"', parameters):
        print('Please replace API_KEY placeholder with your macaddress.io API KEY in parameters.json')
        exit()
    parameters = json.loads(parameters)

def get_query_response(ip):
    api_url = parameters['api_url']
    PARAMS = {'apiKey': parameters['auth_code'],
            'search': ip}
    return requests.get(api_url, params = PARAMS)

response = get_query_response(ip_address)
if response.status_code == 200:
    print("IP Address: {0} \nCompany Name: {1}".format(ip_address, response.content))
else:
    print("Invalid IP Address")

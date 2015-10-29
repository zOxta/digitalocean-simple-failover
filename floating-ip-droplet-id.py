#!/usr/bin/python3

import os
import sys
import requests
import json

api_base = 'https://api.digitalocean.com/v2'

def main():
    headers = {'Authorization': 'Bearer YOU_DIGITAL_OCEAN_API_KEY',
               'Content-type': 'application/json'}
    url = api_base + "/floating_ips"
    r = requests.get(url, headers=headers)

    resp = r.json()
    if 'message' in resp:
        print('{0}: {1}'.format(resp['id'], resp['message']))
        sys.exit(1)
    else:
        print('{}'.format(resp['floating_ips'][0]['droplet']['id']))

if __name__ == "__main__":
    main()
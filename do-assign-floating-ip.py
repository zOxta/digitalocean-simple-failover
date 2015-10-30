#!/usr/bin/python3

import os
import sys
import requests
import json

api_base = 'https://api.digitalocean.com/v2'


def usage():
    print('{} [Floating IP] [Droplet ID]'.format(sys.argv[0]))


def main(floating_ip, droplet_id):
    payload = {'type': 'assign', 'droplet_id': droplet_id}
    headers = {'Authorization': 'Bearer DIGITAL_OCEAN_API_KEY_PLACEHOLDER',
               'Content-type': 'application/json'}
    url = api_base + "/floating_ips/{}/actions".format(floating_ip)
    r = requests.post(url, headers=headers,  data=json.dumps(payload))

    resp = r.json()
    if 'message' in resp:
        print('{0}: {1}'.format(resp['id'], resp['message']))
        sys.exit(1)
    else:
        print('Moving IP address: {}'.format(resp['action']['status']))

if __name__ == "__main__":
    if not len(sys.argv) > 2:
        usage()
        sys.exit()
    main(sys.argv[1], sys.argv[2])

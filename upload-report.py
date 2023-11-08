import requests
import json
import argparse

url_api = "http://18.218.244.166:8080/api/v2/{method}"

def upload (file_report,scan_type,api_key_secret):
    api_key = api_key_secret
    headers = {
        'accept': 'application/json',
        'Authorization': api_key
    }

    report = {
        'file':open(file_report,'rb')
    }

    body = {
        'product_name':'WebGoat',
        'engagement_name':'mario',
        'product_type_name':'Research and Development',
        'active':True,
        'verified':True,
        'scan_type':scan_type
    }

    rrr = requests.post(url_api.format(method='import-scan/'), data=body, files=report, headers=headers, verify=False)
    print(rrr.status_code)
    if rrr.status_code == 201:
        print(json.dumps(rrr.json(), indent=4))
    

if __name__== '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--file','-f', dest='file', help='Nombre del reporte', required=True )
    parser.add_argument('--type-scan','-t', dest='type_scan', help='Nombre del scaner', required=True )
    parser.add_argument('--api-key','-l', dest='api_key_secrets', help='Secreto', required=True )

    args = parser.parse_args()

    upload(args.file, args.type_scan, args.api_key_secret)
import requests
import json
import argparse

url_api = "http://18.218.244.166:8080/api/v2/{method}"
api_key = "Token edaf1740e048924e2f817fb6436a803b690c6900"

def get_products ():
    headers = {
        'accept': 'application/json',
        'Authorization': api_key
    }

    r = requests.get(url_api.format(method = 'products'), headers = headers, verify = False)

    if r.status_code == 200:
        print(json.dumps(r.json(), indent=4))

data = {
    "tags": [
    "string"
  ],
  "name": "string",
  "description": "string",
  "prod_numeric_grade": 2222222222,
  "business_criticality": "very high",
  "platform": "paquito web service",
  "lifecycle": "construction",
  "origin": "third party library",
  "user_records": 2147483647,
  "revenue": "2749397",
  "external_audience": True,
  "internet_accessible": True,
  "enable_product_tag_inheritance": True,
  "enable_simple_risk_acceptance": True,
  "enable_full_risk_acceptance": True,
  "disable_sla_breach_notifications": True,
  "product_manager": 0,
  "technical_contact": 0,
  "team_manager": 0,
  "prod_type": 0,
  "sla_configuration": 0,
  "regulations": [
    0
  ]
}
json_data = json.dumps(data)
def create_product ():
    headers = {
        'accept': 'application/json',
        'Contetnt-Type': 'application/json',
        'Authorization': api_key
    }
    rr = requests.post(url_api.format(method = 'products'), data=json_data, headers = headers, verify = False)
    if rr.status_code == 201:
        print(json.dumps(rr.json(), indent=4))

def upload (file_report,scan_type):
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

    proxy = {
        "http":"http://localhost:8080",
        "https":"http://localhost:8080"
    }

    rrr = requests.post(url_api.format(method='import-scan/'), data=body, files=report, headers=headers, verify=False, proxies = proxy)
    print(rrr.status_code)
    print(json.dumps(rrr.json(), indent=4))
    if rrr.status_code == 201:
        print(json.dumps(rrr.json(), indent=4))
    
if __name__== '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--file','-f', dest='file', help='Nombre del reporte', required=True )
    parser.add_argument('--type-scan','-t', dest='type_scan', help='Nombre del scaner', required=True )

    args = parser.parse_args()

    upload(args.file, args.type_scan)
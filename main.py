import requests
import sys, json
#from requests.auth import HTTPBasicAuth
#import input_auth


#f = open('input_auth.py', 'r')
#content = f.read()
#print(content)


url="http://10.193.147.109:12351/"
#url="http://10.193.147.109:9539/"
url1="http://10.193.147.109:9539/v2/Volumes/"

headers = {"api-key":"91EInPD8i0rM8h2Y2sY12j4rNQRSx5FGZAVPBEIam54qRh3BMXI85Pqs9VfxipoNbObZORpOdlRcaD5yVs3btF0B",
            "secret-key":"QqaveBC2DcinmHrrh71KplcJ1mqm4ATUWMSf8UJ3OM3T8R6s8Mb4uEh4g5fyahAsjnLOFujldS1ACTYa3zos3Vq0",
           "Content-Type": "application/json; charset=utf-8",
           "location":'eu-west1"'
          }


response = requests.get(url + "login/", "headers=headers")
print(response)

resp=requests.get(url1 , "headers=headers")
print(resp)
response.json()
resp.json()
response.raise_for_status()  # raises exception when not a 2xx response


#if response.status_code != 200:
    #print('error: ' + str(response.status_code))
#else:
    #print('Success')
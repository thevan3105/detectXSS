import requests
import urllib
import argparse
# from logging import LOGGER
from urllib.parse import urlparse
from requests.exceptions import ConnectionError

parser = argparse.ArgumentParser()   
parser.add_argument('-u', '--url', required=True)                                                 
parser.add_argument('-w', '--wordlist', required=True)                                           
args = parser.parse_args()
target = args.url
payload = args.wordlist

# print(target)
# print(payload)

def checkDOM_Reflected(target, payload):
    # target = input("Url: ")
    # payload = "<script>alert("");</script>"
    for check in open(payload, "r").readlines():
        # url = target.replace('')
        req = requests.post(target + check)
        if check in req.text:
            print("XSS detected")
            print(check)
        else:
            print("Secure")

def url_validator(target):
    try:
        request = requests.get(target)
    except ConnectionError:
        print('Web site khong ton tai')
    else:
        checkDOM_Reflected(target, payload)

# url_validator(url, payload)
url_validator(target)

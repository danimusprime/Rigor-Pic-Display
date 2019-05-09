import boto3 as bt3
import json
import requests as req
#import credentials


def Wiki_request():
    req.get('https://www.wikiart.org/en/paintings-by-style/socialist-realism?json=2&page=1')

    response = req.get('https://www.wikiart.org/en/paintings-by-style/socialist-realism?json=2&page=1')
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')

in __name__ = main:

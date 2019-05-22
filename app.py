import boto3 as bt3
import json
import requests as req
import pylast
import credentials
from pathlib import Path

def request_status_check():
    response = req.get('https://www.wikiart.org/en/paintings-by-style/socialist-realism?json=2&page=1', params=None)
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')
    return response

def Wiki_request():
    pic_returns = request_status_check()
    json_response = pic_returns.json()
    raw_response = pic_returns.raw
    return json_response
    #print(json_response)

def wiki_headers():
    wiki = request_status_check()
    json_headers = wiki.headers
    #return json_headers
    print(json_headers)

def store_image():
    dataset = 'wiki_images'
    datasets_root = Path('/Users/Danimal/Desktop/Rigor-Pic-Display/Sample Data')

    train_path = datasets_root / 'data.json'
    test_path = datasets_root / dataset / 'test'

    for image_path in train_path.iterdir():
        with image_path.open() as f: # note, open is a method of Path object
            # do something with an image


def upload_images_to_s3(directory):

    for f in directory.iterdir():
        if str(f).endswith(('.png', '.jpg', '.jpeg')):
            full_file_path = str(f.parent) + "/" + str(f.name)
            file_name = str(f.name)
            s3_client.upload_file(full_file_path, settings.BASE_BUCKET, file_name)
            print(f,"put")







if __name__ == "__main__":
    check = request_status_check()
    #req = Wiki_request()
    header = wiki_headers()

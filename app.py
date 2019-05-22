import boto3 as bt3
import json
import requests as req
import pylast
import credentials
import settings
import shutil as sh
import pathlib

def request_status_check():
    '''
    This code was originall designed just to perform the call & validate success
    now peforming an iterative write to file in the given path.
    this currently returns valid json data
    '''
    datasets_path = Path('/Users/Danimal/Desktop/art_test_s3/download.json')
    response = req.get('https://www.wikiart.org/en/paintings-by-style/socialist-realism?json=2&page=1', params=None)
    if response.status_code == 200:
        with open(datasets_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    elif response.status_code == 404:
        print('Not Found.')
    return response

'''
def Wiki_request():
    for page in range(1,10):
        call_url = settings.BASE_URL + settings.STYLE_URL + '&' + settings.PAGINATION_URL + str(page)
        print(page, 'pages processed')
        try:
            response = req.get(call_url, )
        pic_returns = request_status_check()
        json_response = pic_returns.json()
        raw_response = pic_returns.raw
        return json_response
        #print(json_response)

def wiki_headers():
    wiki = request_status_check()
    json_headers = wiki.headers
    return json_headers
    #print(json_headers)

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
'''

if __name__ == "__main__":
    check = request_status_check()
    #req = Wiki_request()
    #header = wiki_headers()

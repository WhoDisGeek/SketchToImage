# imported the requests library
import os
import urllib

import requests

root_path = 'https://storage.googleapis.com/quickdraw_dataset/full/simplified'

# just names
ndjson_list = ['hot air balloon']

for i in ndjson_list:

    file_url = os.path.join(root_path, urllib.parse.quote(i)+'.ndjson')
    print('downloading ', i,' -> ',file_url)
    r = requests.get(file_url)
    file_name = i+'.ndjson'
    with open(file_name , 'wb') as f:
        f.write(r.content)

# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup, UnicodeDammit
import json
import glob
import os


result = dict()
code = ['utf-8', 'utf-16', 'iso-8859-1', 'latin-1']

# database = 'samsung.db'
database = (os.path.abspath(os.curdir).split('/')[-1]) + '.db'


# def encode_key(key):
#    return key.replace('.', '\\u002e').replace('$', '\\u0024')

# def decode_key(key):
#    return key.replace('\\u002e','.').replace('\\u0024','$')

for file in glob.glob("*.php"):
    try:
        DIRNAME = file.split('.')[0]
        soup = BeautifulSoup(open(file, 'rb').read(), 'html.parser')
        temp = {UnicodeDammit(tab.th.string, code).unicode_markup.strip().lower(): [[UnicodeDammit(cell.get_text(
            strip=True), code).unicode_markup.lower() for cell in row("td")]for row in tab("tr")] for tab in soup("table")}
        print(file)
        result[UnicodeDammit(soup.h1.string, code).unicode_markup.lower(
        ).replace("samsung", '').strip()] = {'data': temp, 'icon': DIRNAME + '/icon.jpg', 'images': [img for img in glob.glob(DIRNAME + '/' + '*[0-9]*.jpg')]}
    except Exception as e:
        print("\033[31mFILE- {} with Exception {}\033[39m".format(file, e))

with open(database, 'wb') as json_db:
    json.dump(result, json_db, indent=4)


print("done")

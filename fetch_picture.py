from bs4 import BeautifulSoup
import os
import re
from urllib import request
import glob

ALLFILES = glob.glob('*.php')
un_fetched_files = list()

for count, FILENAME in enumerate(ALLFILES, 1):
    DIRNAME = FILENAME.split('.')[0] + '/'
    img_url = None
    icon_image = None
    images = list()

    def log(string, def_col=''):
        print('\r' + def_col + string + '\033[39m\n' + '\033[1m \033[33m [ {:.1f}% ] \033[39m \033[0m'.format(
            (count * 100) / len(ALLFILES)), end='')

    def img_save(file_name, url):
        try:
            log('openning url {} and saving into file {}'.format(url, file_name))
            temp = request.urlopen(url).read()
            fileopen = open(DIRNAME + '/' + str(file_name) + '.jpg', 'wb')
            fileopen.write(temp)
            fileopen.close()
            log('closing file {}'.format(file_name))
        except Exception as e:
            log('\033[1m \033[31m Error in writing Image {}'.format(file_name))
            log('\033[1m \033[34m Error: {}'.format(e))

    log('opening file {}'.format(FILENAME))
    soup = BeautifulSoup(open(FILENAME, 'rb').read(), 'html.parser')
    try:
        for tags in soup.find_all('a', href=re.compile('pictures')):
            if tags.img:
                img_url = tags.img.parent['href']
                icon_image = tags.img['src']
    except Exception as e:
        log('Error in reading file {}'.format(
            FILENAME), def_col='\033[1m \033[31m')
        log('Error: {}'.format(e), def_col='\033[1m \033[34m')
        continue

    if not os.path.exists(DIRNAME):
        log('creating directory {}'.format(DIRNAME))
        os.mkdir(DIRNAME)
    else:
        log('directory {} is already exist'.format(DIRNAME))
    try:
        if icon_image:
            img_save('icon', icon_image)
        else:
            for tags in soup.find_all('div', attrs={'class': 'specs-photo-main'}):
                icon_image = tags.img['src']
            if icon_image:
                img_save('icon', icon_image)
            else:
                raise KeyError('')
    except:
        log('Error: Icon image not found!', def_col='\033[1m \033[31m')
        un_fetched_files.append(DIRNAME)
        continue

    try:
        if not img_url.startswith('http://'):
            img_url = 'http://gsmarena.com/' + img_url
        soup = BeautifulSoup(request.urlopen(img_url).read(), 'html.parser')
        for tag in soup.find_all('div', attrs={'id': 'pictures-list'}):
            for img in tag.find_all('img'):
                images.append(img['src'])
        if not images:
            raise KeyError('Images directory is empty at remote host')
    except Exception as e:
        log('Error in opening url for image {}'.format(
            img_url), def_col='\033[1m \033[31m')
        log('Error: {}'.format(e), def_col='\033[1m \033[34m')
        continue

    for number, url in enumerate(images):
        img_save(number, url)
    log('{} is successfully fetched!'.format(FILENAME))
if un_fetched_files:
    print("unable to fetched these files")
    for Files in un_fetched_files:
        print('removing -> {}'.format(Files))
        if os.path.exists(Files):
            os.rmdir(Files)
else:
    print('No Errors!')

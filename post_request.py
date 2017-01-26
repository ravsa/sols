from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://ravsa.pythonanywhere.com'  # Set destination URL here
post_fields = {'id': 10, 'name': "testing",
               'password': 123456789}     # Set POST fields here
request = Request(url, urlencode(post_fields).encode())
json = urlopen(request).read().decode()

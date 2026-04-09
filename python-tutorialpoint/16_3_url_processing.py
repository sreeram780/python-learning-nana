from urllib.parse import urlparse
url = "https://example.com/employees/name/?salary>=25000"
parsed_url = urlparse(url)
print (type(parsed_url))
print ("Scheme:",parsed_url.scheme)
print ("netloc:", parsed_url.netloc)
print ("path:", parsed_url.path)
print ("params:", parsed_url.params)
print ("Query string:", parsed_url.query)
print ("Frgment:", parsed_url.fragment)

from urllib.parse import urlparse, parse_qs
url = "https://example.com/employees?name=Anand&salary=25000"
parsed_url = urlparse(url)
dct = parse_qs(parsed_url.query)
print ("Query parameters:", dct)

from urllib.parse import urlunparse
lst = ['https', 'example.com', '/employees/name/', '', 'salary>=25000', '']
new_url = urlunparse(lst)
print ("URL:", new_url)

# from urllib.request import urlopen
# obj = urlopen("https://www.tutorialspoint.com/images/logo.png")
# data = obj.read()
# img = open("img.jpg", "wb")
# img.write(data)
# img.close()

from urllib.request import Request, urlopen
obj = Request("https://www.tutorialspoint.com/")
resp = urlopen(obj)

# from urllib.request import Request, urlopen
# obj = Request("https://www.tutorialspoint.com/")
# resp = urlopen(obj)
# data = resp.read()
# print (data)

from urllib.request import Request, urlopen
import urllib.error as err

obj = Request("http://www.nosuchserver.com")
try:
   urlopen(obj)
except err.URLError as e:
   print(e)

from urllib.request import Request, urlopen
import urllib.error as err

obj = Request("http://www.python.org/fish.html")
try:
   urlopen(obj)
except err.HTTPError as e:
   print(e.code)
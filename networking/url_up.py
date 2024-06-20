# import urllib.request
# print(urllib.request.urlopen("https://www.stackoverflow.com").getcode())

# import httplib
# conn = httplib.HTTPConnection("www.python.org")
# conn.request("HEAD", "/")
# r1 = conn.getresponse()
# print r1.status, r1.reason

import http.client
host = "docs.python.org"
conn = http.client.HTTPSConnection(host)
conn.request("GET", "/3/", headers={"Host": host})
response = conn.getresponse()
print(response.status, response.reason)
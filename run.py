from typing import OrderedDict
import requests

s = """Host: ariela2015.tau.ac.il
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Connection: keep-alive
Referer: http://ariela2015.tau.ac.il/F?RN=1000000
Upgrade-Insecure-Requests: 1"""

params = {
    'func':'find-b',
    'find_code':'WRD',
    'local_base':'SZ', # change for another location
    'adjacent':'N',
}

url = 'http://ariela2015.tau.ac.il/F/7SCDKVD3JP8R96ETR6JA86RE5BLMIVDGY9R38FU1I9LPHCQ47L-54854' # change the number in the end and the file name?

WORD = 'ביוור סטלינגרד'
params['request'] = WORD

parse_headers = lambda headers: OrderedDict(row.split(': ') for row in headers.split('\n'))

res = requests.get(url=url, params=params)

with open('res.html', 'wb') as f:
    f.write(res.content)

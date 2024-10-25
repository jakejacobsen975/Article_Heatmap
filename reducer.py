#!/bin/python3

import sys
import json
ksl = ""
cnbc = ""
the_verge = ""
abc = ""
cbs = ""

for line in sys.stdin:
    line = line.strip()
    if line:
        url, content = line.split(':::')
        if 'ksl.com' in url:
            ksl += content
        elif 'cnbc.com' in url:
            cnbc += content
        elif 'theverge.com' in url:
            the_verge += content
        elif 'abcnews.go' in url:
            abc += content
        elif 'www.cbsnews.com' in url:
            cbs += content
        


all_articles = [ ksl, cnbc,the_verge]
print(json.dumps({'ksl':ksl}))
print(json.dumps({'cnbc':cnbc}))
print(json.dumps({'abc':abc}))
print(json.dumps({'cbs':cbs}))
print(json.dumps({'the verge':the_verge}))






TOKEN = '5510877429:AAHRmt6-cGRm4fqEEPbsY0ZtYDfZ5HtyXk0'


import json


ar = []

with open('cenz.txt', encoding='utf8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            ar.append(n)

with open('cenz.json', 'w', encoding='utf-8') as e:
    json.dump(ar, e)
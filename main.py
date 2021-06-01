import re
import json
import requests

#
# with open('countries.json') as f:
#     templates = json.load(f)
#     data = json.dumps(templates)
#     # print(data)
#
#     names = re.findall('("name": {"common":)''(.*?)''("official":)' ,data)
#     print(names)

class Json_one_iterate():
    def __iter__(self):
        with open('countries.json') as f:
            data = json.load(f)
            self.x = re.findall('("name": {"common":)''(.*?)''("official":)', data)
            # print(self.x)
        return self
    def __next__(self):
        t = next(self.x)
        return t

pages = Json_one_iterate()
for names in pages:
    print(names)

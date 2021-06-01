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
            self.x = iter(re.findall('("name": {"common":)''(.*?)''("official":)', data))
            # self.x = iter(set(re.findall('("name": {"common":)''(.*?)''("official":)', data)))
            # print(self.x)
        return self
    def __next__(self):
        t = self.x.pop()
        return t.text

pages = tuple(Json_one_iterate())
print(pages)
# for names in pages:
#     print(names)

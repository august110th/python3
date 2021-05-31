import re
import json
import requests


with open('countries.json') as f:
    templates = json.load(f)
    data = json.dumps(templates)
    # print(data)

    names = re.findall(r'("name": \s("common":\s").+(?=",[\s\S]+"official")', data)
    print(names)



# json_one = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"
#
#
# class Json_one_iterate():
#
#     def __iter__(self):
#         self.counter = 1
#         with open('countries.json') as f:
#             templates = json.load(f)
#             self.x = (templates[self.counter]['name']['common'])
#             # print(self.x)
#         return self
#
#     def __next__(self):
#         return self
#
#
#
# pages = Json_one_iterate()
# for names in pages:
#     print(names)
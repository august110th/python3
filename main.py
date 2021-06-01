import re
import json
import requests

#
with open('countries.json') as f:
    templates = json.load(f)
    data = json.dumps(templates)
    # print(data)

    names = re.findall('("name": {"common":)''(.*?)''("official":)' ,data)
    print(names)
# #
# #
# #
# # # json_one = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"
# # #
# # #
# # class Json_one_iterate():
# #     def __init__(self):
# #         self.counter = 1
# #
# #     def __iter__(self):
# #         with open('countries.json') as f:
# #             templates = json.load(f)
# #             self.x = (templates[self.counter]['name']['common'])
# #             # print(self.x)
# #         return self
# #     def __next__(self):
# #         self.counter += 1
# #         t = next(self.x)
# #         return t
# # # #
# # # #
# # # #
# # pages = Json_one_iterate()
# # for names in pages:
# #     print(names)
# # # with open('countries.json') as f:
# # #     templates = json.load(f)
# # #     print(templates[2]["name"]["common"])
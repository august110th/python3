import re
import json
import requests
import pprint

with open('countries.json') as f:
    templates = json.load(f)
    x = re.findall("name", templates)
    print(x)



# json_one = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"


# class Json_one_iterate():
#     def __iter__(self):
#         with open('countries.json') as f:
#             templates = json.load(f)
#             x = iter(set(re.findall(r'', templates)))
#             # print(x)
#         return self
#         # response = requests.get(json_one)
#         # main_page = response.text
#
# #         print(main_page)
# #         self.links = iter(set(re.findall(r'"common": "(.*?)","official"', main_page)))
# #         return
# #
# #     def __next__(self):
# #         link = next(self.links)
# #         return requests.get(link).text
# # #
# #
# pages = tuple(Json_one_iterate())
# print(pages)
# # pages = Json_one_iterate
# # for item in pages:
# #     print(item)
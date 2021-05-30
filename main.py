import re
import json
import requests


# with open('countries.json') as f:
#     templates = json.load(f)
#     print(templates[1]['name']['common'])



json_one = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"


class Json_one_iterate():
    def __iter__(self):
        with open('countries.json') as f:
            templates = json.load(f)
        return self

    def __next__(self):
        link = next(self.links)
        return requests.get(link).text
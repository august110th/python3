import re

import requests
json_one = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"

class Json_one_iterate():
    def __iter__(self):
        response = requests.get(json_one)
        main_page = response.text
        self.links = iter(set(re.findall(r'"name": "common":', main_page)))
        return self
    def __next__(self):
        link = next(self.links)
        return requests.get(link).text

pages = tuple(Json_one_iterate())
print(pages)
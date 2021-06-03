import json


def json_reader(file):
    with open(file.encode()) as f:
        names = json.load(f)
        print(names)
    return names
def writer_txt(file, names_list, line_number):
    with open(file, "a+", encoding='utf-8') as f:
        country = names_list[line_number]['name']['common']
        url = f'https://en.wikipedia.org/wiki/' + country
        f.write(f'{country} - {url}\n')

class Json_iterator:
    def __init__(self, line_number):
        self.line_number = line_number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.line_number:
            writer_txt('countries.txt', file_json, self.counter)
            self.counter += 1
        else:
            raise StopIteration
file_json = json_reader("countries.json")
iterator = [country for country in Json_iterator(250)]
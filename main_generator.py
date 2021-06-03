import json
import hashlib

def generator():
    with open('countries.json') as f:
        names = json.load(f)
    for line in names:
        yield hashlib.md5(line)


d = generator()
print(d)

# hash_object = hashlib.md5(b'Hello World')
# print(hash_object.hexdigest())
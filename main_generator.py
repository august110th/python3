import json
import hashlib

def generator():
    with open('countries.json') as f:
        names = json.load(f)
    for line in names:
        yield hashlib.md5(str(line).encode('utf-8')).hexdigest()

for hash in generator():
    print(hash)
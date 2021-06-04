import json
import hashlib

# def generator():
#     with open('countries.json') as f:
#         names = json.load(f)
#     for line in names:
#         yield line
#         hashlib.md5(line).hexdigest()


# for x in generator():
#     print(type(x))
# # print(d)

# hash_object = hashlib.md5(b'Hello World')
# print(hash_object.hexdigest())

with open('countries.json') as f:
    names = json.load(f)
    data = json.dumps(names)
    # print(type(names))
    # print(type(data))
    for line in names:
        h = str(line)
        hashlib.md5(h.encode('utf-8')).hexdigest()
        print(h)
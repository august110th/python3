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
    # print(type(names))
    for line in names:
        h = hashlib.md5(str(line).encode('utf-8'))
        print(h)
book = {}
book["tom"] = {
    "name": "Tom",
    'addres': "1 red street",
    'phone': 321313
}

book["bob"] = {
    "name": "Bob",
    'addres': "2 red street",
    'phone': 312312
}

import json
s = json.dumps(book)
print(s)

with open("D:\AI Engineer\AIEngineer\python\data/book.txt","w") as f:
    f.write(s)

f = open("D:\AI Engineer\AIEngineer\python\data/book.txt","r")
s = f.read()
print(s)

import json
book = json.loads(s)
print(book)

print(type(book))

for person in book:
    print(book[person])
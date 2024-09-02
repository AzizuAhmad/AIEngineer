# dictionary

d = {"tom":1234,"rob":333,"rangga":635}
print(d)

print(d["rob"])

d["sam"] = 8788

print(d)

del d["sam"]
print(d)

for key in d:
    print(key,d[key])

print(d.items())

for k,v in d.items():
    print("key : ",k,"value : ",v)

# Tuples
point =(5,9)
print(point)
print(point[1])

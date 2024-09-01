exp = [2340, 2500, 2100, 3100, 2980]

total = 0

for i in exp:
    total = total + i
    print(total)

print(total)

for i in range(1,11):
    print(i*i)


total = 0
for i in range(len(exp)):
    print("month : ",(i+1), "expanse : ",exp[i])
    total = total + exp[i]
   
print("total expanse : ",total)


keyLocation = "chair"

location = ["garage","living room","chair","closet"]

for i in location:
    if i == keyLocation:
        print("key is found in ",i)
        break
    else:
        print("key is not found in ",i)

i = 1
while i <= 5:
    print(i)
    i = i+1
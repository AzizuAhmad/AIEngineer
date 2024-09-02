def calculate(exp):
    total = 0
    for item in exp:
        total =  total + item
    
    return total

tomExp =  [2000,3213,4124]
joeExp = [3211,6452,3211]

tomsTotal = calculate(tomExp)
JoesTotal = calculate(joeExp)

print(tomsTotal)
print(JoesTotal)

def sum(a,b):
    print(f"a : {a}")
    print(f"b : {b}")

    total = a+b
    print(f"total : {total}")
    # return total

n = sum(5,6)
# print(n) 
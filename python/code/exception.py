x = input("enter number 1 : ")
y = input("enter number 2 : ")

try:
    z = int(x) / int(y)
except ZeroDivisionError as e:
    print("Division by zero exceptions : ")
    z = None
print("Division is : ",z)
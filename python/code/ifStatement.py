num = input("enter a number: ")
num = int(num)

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

indian = ["samosa","daal","naan"]
chines = ["egg role","pot sticker","fried rice"]
italian = ["pizza","pasta","lasagna"]

dish = input("enter a dish nme : ")

if dish in indian:
    print("indian")
elif dish in chines:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("unknown")
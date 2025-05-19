a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if a+b > c and a + c > b and c + b > a:
    print("Valid, you can make a triangle")
else:
    print("Invalid, you can't make a triangle with these sides.")
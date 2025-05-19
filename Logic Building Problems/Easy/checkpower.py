x = int(input("Enter x: "))
y = int(input("Enter y: "))

n = 0
while x**n <= y:
    if x**n == y:
        print("True")
        break
    n += 1
else:
    print("False")
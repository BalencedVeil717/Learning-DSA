n = int(input("Enter number: "))
new = 0

while n:
    last = n % 10
    new = new*10 + last
    n = n//10
print(new)


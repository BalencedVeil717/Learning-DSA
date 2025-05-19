n = int(input("Enter number: "))
c = 0
for a in range(n+1):
    for b in range(n +1):
        if a**3 + b**3 == n:
            c+=1
print(c)
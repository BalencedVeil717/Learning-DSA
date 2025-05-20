a = int(input("Enter a: "))
b = int(input("Enter b "))

m = min([a,b])
f = []
for i in range(1,m+1):
    if a%i == 0 and b%i == 0:
        f.append(i)
    
print(max(f))


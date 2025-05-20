a = int(input("Enter a: "))
b = int(input("Enter b: "))

t = (a, b)

greater = max(t)
smaller = min(t)

for i in range(greater, a * b + 1, greater):
    if i % smaller == 0:
        print("LCM is", i)
        break

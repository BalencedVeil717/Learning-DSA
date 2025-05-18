a1 = int(input("Enter first term: "))
a2 = int(input("Enter second term: "))
n = int(input("Enter nth term to find: "))
d = a2 - a1
term = a1 + (n - 1) * d
print("Nth term =", term)

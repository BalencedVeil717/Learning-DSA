# Given two integers n and m (m != 0). Find the number closest to n and divisible by m.

n = int(input("Enter n: "))
m = int(input("Enter m: "))
diff = {}

for i in range(n - m, n + m + 1):
    if i % m == 0:
        diff[abs(n - i)] = i

print(diff[min(diff.keys())])

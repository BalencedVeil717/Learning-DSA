l1 = [0, 10]
r1 = [10, 0]
l2 = [5, 5]
r2 = [15, 0]

of1 = []
of2 = []

for i in range(r1[0],l1[0]-1,-1):
    of1.append([i,r1[1]])
for i in range(r1[1],l1[1]+1):
    of1.append([r1[0],i])
for i in range(l1[0],r1[0]+1):
    of1.append([i,l1[1]])
for i in range(l1[1],r1[1]-1,-1):
    of1.append([l1[0],i])

for i in range(r2[0],l2[0]-1,-1):
    of2.append([i,r2[1]])
for i in range(r2[1],l2[1]+1):
    of2.append([r2[0],i])
for i in range(l2[0],r2[0]+1):
    of2.append([i,l2[1]])
for i in range(l2[1],r2[1]-1,-1):
    of2.append([l2[0],i])

for i in of1:
    if i in of2:
        print("Overlap")
        break
else:
    print("Not overlap")
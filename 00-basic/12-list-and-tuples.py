
x = 6, 7, 8, 9
y = (6, 7, 8, 9)

z = [6, 7, 8, 9]

print(x[1])
print(y[2])
print(z[3])

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 123, 31]

l.append(2)
print(l)

l.insert(1, 100)
print(l)

l.remove(100)
print(l)

print(l[4:])
print(l[:4])
print(l[:-4])
print(l[:])
print(l.count(6))
l.sort()
print(l)

l2 = [
    [1, 3, 4, 5, 7],
    [2, 3, 4, 5, 7],
    [3, 3, 4, 5, 7],
    [4, 3, 4, 5, 7],
    [6, 3, 4, 5, 7],
    [7, 3, 4, 5, 7]
]
print(l2[1][2])

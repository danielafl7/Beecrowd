j, r = [int(x) for x in input().split()]
l = list(map(int, input().split()))

x = [0]*j

for i in range(j):
    x[i] = sum(l[i::j])

x = x[::-1]
w = j - x.index(max(x))

print("{:d}".format(w))

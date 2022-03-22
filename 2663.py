n = int(input())
k = int(input())

l = [int(input()) for i in range(n)]
l.sort(reverse=True)

c=k

while c<n and l[c]==l[k-1]:
    c = c + 1

print("{:d}".format(c))

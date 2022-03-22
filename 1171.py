n = int(input())
l = list()

for i in range(n):
    l.append(int(input()))
    
x = {}
for a in map(str, sorted(l)):
    if not a in x:
        x[a] = 1 
    else:
        x[a] = x[a] + 1

for a in x:
    print("{:d} aparece {:d} vez(es)".format(int(a), x[a]))
    

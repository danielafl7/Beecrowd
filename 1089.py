while True:
    n = int(input())
    if (n==0):
        break
    
    l = list(map(int,input().split()))
    l.append(l[0])
    l.append(l[1])
    s = 0
    
    for i in range(1, n+1):
        if (l[i] < l[i+1] and l[i] < l[i-1]):
            s = s+1
        elif (l[i] > l[i+1] and l[i] > l[i-1]):
            s = s+1
    
    print("{:d}".format(s))

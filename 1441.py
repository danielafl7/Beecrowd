def h(n):
    if (n%2==0): 
        return int(n//2)
    else: 
        return 3*n+1

while True:
    n = int(input())
    x = n
    
    if (n==0): 
        break
    
    
    while n!=1:
        if (x<n): 
            x=n
        n = h(n)
    
    print("{:d}".format(x))

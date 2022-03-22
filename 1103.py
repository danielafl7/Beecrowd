while True:
    h1, m1, h2, m2 = [int(x) for x in input().split()]
    
    if (h1==0 and m1==0 and h2== 0 and m2==0): 
        break
    
    x = (h2*60 + m2) - (h1*60 + m1)
    x = x+1440 if x<=0 else x
    
    print("{:d}".format(x))

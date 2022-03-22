t = int(input())

for i in range(t):
    pa,pb,g1,g2 = map(float,input().split())
    x = 0
    
    while(pa<=pb):
        cpa = int((pa*(g1/100)))
        cpb = int((pb*(g2/100)))
        x = x + 1
        pa = pa + cpa
        pb = pb + cpb
        
        if(x > 100):
            break

    if(x>100):
        print("Mais de 1 seculo.")
    
    else:
        print("{:d} anos.".format(x))

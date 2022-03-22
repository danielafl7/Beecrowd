def soma(x):
    if len(x)==1: 
        return x
    
    s = 0
    
    for i in range(len(x)):
        s = int(x[i]) +s
    
    return soma(str(s))

while True:
    e = str(input()).split()
    n = e[0]
    m = e[1]
    
    if (n==m=="0"): 
        break
    
    tn = soma(n)
    tm = soma(m)
    
    if tn>tm: 
        print("1")
    elif tn<tm: 
        print("2")
    else: 
        print("0")

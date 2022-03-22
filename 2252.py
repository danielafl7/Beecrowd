c = 1

while True:
    try:
        n = int(input())
        v = list(map(float,input().split()))
        pw = []
        
        for i in range(n):
            x = v.index(max(v))
            pw.append(x)
            v[x] = -1
        
        print("Caso {}: ".format(c),*pw , sep='')
        c = c + 1
    
    except EOFError:
        break

n=int(input())
c=0
r=0
s=0

for i in range(n):
    a,b=list(map(str,input().split()))
    a=int(a)
    if(b == "C"):
        c = c+a
    elif (b == "R"):
        r = r+a
    else:
        s = s+a
        
t=c+r+s
pc=(c*100.00)/t
pr=(r*100.00)/t
ps=(s*100.00)/t

print("Total: {} cobaias".format(t))
print("Total de coelhos: {}".format(c))
print("Total de ratos: {}".format(r))
print("Total de sapos: {}".format(s))
print("Percentual de coelhos: {:.2f} %".format(pc))
print("Percentual de ratos: {:.2f} %".format(pr))
print("Percentual de sapos: {:.2f} %".format(ps))

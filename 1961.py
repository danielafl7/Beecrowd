p,n = map(int,input().split())
altura = list(map(int,input().split()))

x = True

for i in range(0,len(altura)-1):
    if (abs(altura[i]-altura[i+1])>p):
        x = False
    
if (x == True):
    print("YOU WIN")
   
else:
    print("GAME OVER")

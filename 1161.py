def fatorial(x):
  fat=1
  for i in range(1,x+1):
    fat= fat*i
  return fat

while True:
  try:
    m,n = map(int,input().split())
    fatorialm = fatorial(m)
    fatorialn = fatorial(n)    
    soma = fatorialm + fatorialn
    
    print("{:d}".format(soma))
  
  except EOFError:
    break 

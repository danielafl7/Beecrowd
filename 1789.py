while True:
    
  v = list
  
  try:
    l = int(input())
    v=[int(y) for y in input().split()]
    
    for i in range(len(v)):
      v[i] = int(v[i])

    if (max(v)<10):
      print("1")
      
    elif (max(v)>=20):
      print("3")
      
    elif (max(v)>=10 or max(v)<20):
      print("2")
      
  except EOFError:
      break

x = 0
while True:
    Lista = []
    L1 = []
    L2 = []
    L3 = []
    L4 = []

    x = x + 1
    n = int(input())

    if (n==0):
        break

    for i in range(n):
        r = list(map(int, input().split()))
        Lista.append(r)
        L1.append(r[0])
        L2.append(r[1])
        L3.append(r[2])
        L4.append(r[3])

    I1 = max(L1)
    I2 = min(L2)
    I3 = min(L3)
    I4 = max(L4)

    print("Teste {0}".format(x))

    if (I1<I3 and I2>I4):
        print("{0} {1} {2} {3}".format(I1, I2, I3, I4))
        print()
    else:
        print("nenhum")
        print()

def pisagor():
    n=1
    x=int(input("sayın"))
    for a in range(1,x+1):
        for b in range(1,x+1):
            for c in range(1,x+1):
                if (c**2 == a**2+b**2 and b > a):
                    print(a,b,c)
                else:
                    continue
pisagor()

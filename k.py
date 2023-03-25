def i ():
    q = 0
    b = 0
    t = 0
    a = int(input("sayaınız"))
    while b == a:
        q = q + 1
        if a % q == 0:
            b = b + q
        elif q > a:
            print("no")
            break
        else:
            continue
    if b == a:
        print(a)
    else:
        print("no")
i()

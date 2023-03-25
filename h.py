while True:
    def işleminiz(a):
        if a == "*":
            b=int(input("birinci sayı"))
            c = int(input("ikinci sayı"))
            b = b * c
            print(b)
        elif a == "+":
            b = int(input("birinci sayı"))
            c = int(input("ikinci sayı"))
            b = b+c
            print(b)
        elif a=="-":
            b = int(input("birinci sayı"))
            c = int(input("ikinci sayı"))
            b = b-c
            print(b)
        elif a=="/":
            b = int(input("birinci sayı"))
            c = int(input("ikinci sayı"))
            b = b/c
            print(b)
        elif a=="**":
            b = int(input("birinci sayı"))
            c = int(input("ikinci sayı"))
            b = b**c
            print(b)


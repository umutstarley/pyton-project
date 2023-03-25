print("faktoryel bulma programı")
print("çıkmak için a")


while True:
    sayı = input("sayı:")
    if(sayı == "a"):
        print("baybay")
        break
    else:
        sayı=int(sayı)

        faktoryel = 1
        for i in range(2,sayı+1):
            print("faktoriyel",faktoryel,"i:",i)
            faktoryel *= i
        print("faktoriyel ",faktoryel)





    if s % 2 == 0:
        print("çift")
    else:
        print("tek")
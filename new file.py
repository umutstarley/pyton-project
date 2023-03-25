def ekok(a,b):
    ortak=[]
    carpim =a*b
    for i in range(1,a+1):
        for j in range(1,b+1):
            if a % i==0 and b % j==0:
               carpim *= i

               ortak.append(i)


    c=a*b/ortal
    print(c)
b = int(input("büyük sayınız"))
a = int(input("küçük sayınız"))
ekok(a,b)
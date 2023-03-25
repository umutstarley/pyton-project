q=0
b=0
t=0
a = int(input("sayaınız"))
while b==1000:
    q = q+1
    if a % q == 0:
        b =b+ q
    elif q>a:
        print("no")
        break
    else:
        continue
if b==a:
    print(a)
else:
    print("no")


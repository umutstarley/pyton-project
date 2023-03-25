def asal(w):
    if w == 1:
        return False
    elif w == 2:
        return
    else:
        for i in range(2,w):
            if (w % i == 0):
                return False
        return True
while True:
    a = input("çıkmak için q")
    if a == "q":
        break
    else:
        asal(int(input("sayınız")))
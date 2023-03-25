birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar=["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def oku(s):
    birinci = s%10
    ikinci =s//10

    return onlar[ikinci]+" "+birler[birinci]

s=int(input("sayı:"))
print(oku(s))
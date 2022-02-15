"""
Kullanıcının girdiği bir değere göre çarpım tablosu oluşturan programı kodlayınız. 
"""
sayi= int(input("Kaclar tablosu yapilacak: "))
for m in range(11):
    print(sayi,"x",m,"=",m*sayi)
    m += 1

#Ekstra Cozum
"""
m=0
sayi=int(input("Hangi sayinin carpim tablosunu istiyorsunuz: "))
while(m<10):
    print(m*sayi)
    m += 1
 
"""

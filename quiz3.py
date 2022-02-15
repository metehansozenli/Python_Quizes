"""
Kullanıcının girdiği bir değere göre çarpım tablosu oluşturan programı kodlayınız. 
"""
sayi= int(input("Kaclar tablosu yapilacak: "))
for m in range(11):
    print(sayi,"x",m,"=",m*sayi)
    m += 1

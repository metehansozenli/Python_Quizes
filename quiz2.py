"""
Python'da liste yapılarını kullanarak 5 adet il adı içeren bir liste oluşturunuz.
Kullanıcıdan bir adet sayı alınız. Kullanıcıdan girilen sayı listenin kaçıncı elemanına denk geliyorsa bu ilin ilk 2 ve son 2 karakterini ekrana basacak bir program yazınız. 
Örneğin listemizdeki ilk il "istanbul" olsun. Kullanıcıdan aldığımız sayı 0 ise ekrana İstanbul ilinin ilk 2 ve son 2 harfini alarak ekrana "İsul" yazacak. 
Özetle kullanıcı 0,1,2,3,4 rakamlarından birini girmiş ise bu rakamlara karşılık gelen il adının ilk 2 ve son 2 harfi ekrana yazılacaktır. 
"""
sehirler= ["tokat", "bursa","ankara","istanbul","izmir"]

sayi= int(input("Bir sayı girin: "))

if sayi == 0:   
    print ((sehirler[sayi][0:2])+(sehirler[sayi][-2:]))
elif sayi ==1:
    print ((sehirler[sayi][0:2])+(sehirler[sayi][-2:]))
elif sayi== 2:
    print ((sehirler[sayi][0:2])+(sehirler[sayi][-2:]))
elif sayi== 3:
    print ((sehirler[sayi][0:2])+(sehirler[sayi][-2:]))    
elif sayi == 4:
    print ((sehirler[sayi][0:2])+(sehirler[sayi][-2:]))
else:
    print("Yanlış sayi")

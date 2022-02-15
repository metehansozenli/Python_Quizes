"""
Kullanıcıdan alacağınız x ve y değerlerine karşılık gelen (x,y) noktasının "r" yarıçağlı çemberin içinde olup olmadığını kontrol  eden python fonksiyonu yazınız. 
Eğer verilen nokta çemberin içindeyse 1 sonucunu, değilse 0 sonucunu döndürecektir.
Not: Sadece fonksiyonu yazmanız yeterlidir.  Fonksiyon şu değişkenleri alacak ve şu adlı olacaktır.
cemberkontrol( r , x , y )
"""
def cemberkontrol(r,x,y):
    if ((x*x) + (y*y)<=(r*r)):
        return(1)

    else :
        return(0)

r=5
x=int(input("x değerini girin: "))
y=int(input("y değerini girin: "))

sonuc=cemberkontrol(r,x,y)

print(sonuc)


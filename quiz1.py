"""
il" adlı değişkene herhangi bir il adlı girildiğinde bu ilin ilk harfini ve sonrasında aradaki her harf kadar "*" işaret ve ilin son harfini basacak şekilde 
print ifadesinin içinde boş bırakılan yeri doldurunuz. Örneğin il istanbul girilmişse i******l  yazacak fakat il bursa girilmişse b***a yazacaktır.
"""
il="Tokat"
print(il[0]+((len(il)-2)*"*")+il[-1])

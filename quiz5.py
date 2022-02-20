""" 
"once.txt" adlı dosyayı python ile okuyup içinceki metinlerin tamamını her bir karakterden sonra bir boşluk olacak şekilde düzeleyerek "sonra.txt" adlı 
dosyaya yazacak python kodunu yazınız.
"""
with open ("once.txt","r") as file:
    okunan = file.read()
    okunan2 = ""

    for i in okunan:
        okunan2 = okunan2 + " " + i

with open ("sonra.txt","w") as file_write:
    file_write.write(okunan2)
    

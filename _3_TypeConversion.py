x=input("1.sayı: ")
y=input("2.sayı: ")

# input metodu ile kullanıcıdan string tipinde aldığımız verileri değişkenlere atıyoruz
toplam=x+y
print("Dönüşümsüz Toplama: ",toplam)

toplam=int(x)+int(y)
# matematiksel bir toplama işlemi gerçekleştirebilmek için string tipindeki sayı verilerini int tipine dönüştürüyoruz
print("Dönüşümlü Toplama: ",toplam)

print()

# int ve float veri tipleri arasında dönüşüm gerçekleştirelim
sayi=10
print("Sayı: ",sayi)
print("Sayi değişkeninin tipi: ",type(sayi))

floatSayi=float(sayi)
print("Float'a dönüşüm sonrası Sayı: ",floatSayi)
print("Sayi değişkeninin tipi: ",type(floatSayi))

del toplam # önceden tanımladığımız toplam değişkenini siliyoruz
toplam=str(sayi)+str(floatSayi) # int ve float türündeki değişkenleri string türüne çevirip topluyoruz
print(toplam)

isOnline=True
print("Dönüşüm öncesi isOnline değeri: ",isOnline)
isOnline=int(isOnline)
print("Dönüşüm sonrası isOnline değeri: ",isOnline)



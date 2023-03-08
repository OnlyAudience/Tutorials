from datetime import datetime 
#from datetime ifadesi ile datetime modülüne erişim sağlıyoruz, import ile modülün içerisindeki datetime sınıfını programımıza dahil ediyoruz.

# Müşteri için çeşitli bilgilerini atayabileceğimiz değişkenlerimizi tanımlıyoruz

musteriAdi="Ali"
musteriSoyad='Yılmaz'
musteriAdSoyad=musteriAdi+" "+musteriSoyad
musteriCinsiyet= True # Erkek
musteriTC_Kimlik='30255442901'
musteriDogumYili=1989
musteriAdresi='İstanbul Kadıköy'


print("Müşteri Adı ve Soyadı",musteriAdSoyad)
mCinsiyet="Erkek" if musteriCinsiyet else "Kadın"
# Ternary Operatörü ile musteriCinsiyet değişkenine göre cinsiyet bilgisini Erkek-Kadın olarak tanımlıyoruz
print("Müşteri Cinsiyeti: ",mCinsiyet)
print("Müşteri TC Kimlik: ",musteriTC_Kimlik)
print("Müşteri Adresi: " ,musteriAdresi)

suankiSene=datetime.now().year 
# şuan ki tarih bilgisini alıyoruz ve yalnızca yıl bilgisini değişkenimize tanımlıyoruz
musteriYasi=suankiSene-1989
print("Müşteri Yaşı:" ,musteriYasi)
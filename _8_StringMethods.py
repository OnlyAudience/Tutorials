message=' Hello There. My name is Erdem Kantos '

# message=message.upper() # upper ile tüm string karakterlerini büyük harfe dönüştürebiliriz.
# print(message)

# message=message.lower() # lower ile tüm string karakterlerini küçük harfe dönüştürebiliriz.
# print(message)

# message=message.title() # title ile kelimenin baş harflerini bu şekilde büyük harfe dönüştürebiliriz.
# print(message)

# message=message.capitalize() # capitalize ile yalnızca stringin ilk karakterini büyük harfe dönüştürebiliriz
# print(message)

print("Strip öncesi string uzunluğu: "+str(len(message)))
message=message.strip() # strip metodu ile string ifadesinin baş ve sonundaki boşlukları kaldırabiliriz
print("Strip öncesi string uzunluğu: "+str(len(message)))
print(message)
print()

# message=message.split('.') 
# print(f"String Dizesi: {message}\n String Dize Uzunlugu: {len(message)}")
# split ile bir karakter belirtmeden veya belirterek bütün haldeki string dizesini bölebiliriz

# message=message.split()
# print(f"String Dizesi: {message}\n String Dize Uzunlugu: {len(message)}")

# message=' '.join(message) # join metodu ile ayrıştırdığımız string dizesini belirteceğimiz ara karakter ile birleştirebiliriz
# print(f"String Dizesi: {message}\n String Dize Uzunlugu: {len(message)}")

# findIndex=message.find('Erdem') # find metodu ile string içerisinde arayabilir, bulunması durumunda ilk index bilgisini elde edebiliriz.
# print(findIndex) 

# findStart=message.startswith('H') # startswith ile string dizesinin ilk karakteri için bir kontrol işlemi gerçekleştirebiliriz
# print(findStart) # String dizesinin metot içerisinde verdiğimiz parametre ile başlaması durumunda metot bize True değeri döndürecektir.

# findEnd=message.endswith('K') #endwith ile string dizesinin son karakteri için bir kontrol işlemi gerçekleştirebiliriz.
# print(findEnd) # String dizesinin son karakteri metota parametre olarak verdiğimiz karakter ile uyuşmaması durumunda metot bize False değeri döndürecektir

# message=message.replace('Erdem','Mehmet') # replace ile string dizesi içerisinde belirttiğimiz ilk parametreyi arayabilir ve ikinci parametre ile ilgili dönüşümü sağlayabiliriz.
# print(message)
# Aynı dize üzerinde birden fazla replace kullanarak boşluk, türkçe karakter gibi sorun oluşturabilecek ifadeleri toplu bir şekilde değiştirebiliriz.
message=message.center(50,'*') #center metodu belirttiğimiz uzunlukta bir container oluştururak string dizisini belirttiğimiz karakterler arasına ortalı bir şekilde yerleştirir. 
print(message)

# count ile string ifadesi içerisinde bir karakterden kaç adet bulunduğunu öğrenebiliriz
text="merhaba"
karakter="a"
adet=text.count(karakter)
print(f"{text} içerisinde {karakter} karakterinden {adet} bulunmakta.")
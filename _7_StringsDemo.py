website="http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- 'course' karakter dizisi karakter sayısı nedir?
print("Course karakter dizisi: {} karakterden oluşmaktadır".format(len(course)))

# 2- 'website' içinden www karakterlerini alın.
print(website[7:10])

# 3 - 'website' içinden com karakterlerini alın.
print(website[len(website)-3:])

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
print(course[:15]+"\n"+course[len(course)-15:])

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
print(course[::-1])

# Bir string ifades * işareti ile birden fazla kez atayıp [::5] ifadesi ile her 5 karakterden 1'ini ekrana yazdıralım
sayi='12345'*5
print(sayi[::5])

name, surname, age, job='Bora','Yılmaz',32,'mühendis'
# 6 - Yukarı da verilen değişkenler ile ekrana aşğıdaki ifadeyi yazdıralım
# 'Benim adım Bora Yılmaz, Yaşım 32 ve "mesleğim" mühendis.'
print(f'Benim adım {name} {surname}, Yaşım {age} ve "mesleğim" {job}.')
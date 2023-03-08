maasAli=5000
maasAhmet=4000
vergi=0.27

print(maasAli-(maasAli*vergi))
print(maasAli-(maasAhmet*vergi))

# Değişken Tanımlama Kuralları
# Değişken isimleri rakam ile başlayamaz, _ ile başlayabilir veya rakam ile bitebilir.
numberOne=10
print(numberOne)

_number2=20
print(_number2)

_number2+=numberOne
print(_number2)

# Türkçe karakter kullanmamalıyız

x=1             # int
y= 2.3          # float
name="Çınar"    # string
isStudent=True  # bool

strFirstNo='10'
strSecondNo='15'
print(strFirstNo+strSecondNo)

# + Operatörü String değişkenlerinde metin karakterlerini ardarda birleştirmeye, yazmaya yarar.

firstName="Erdem"
lastName=" Kantos"
print(firstName+lastName)

# Değişken isimlerinde boşluk kullanmamalıyız
# Farklı türlerde dahi olsa birden fazla değişkeni tek satırda tanımlayabiliriz

numberVariable,floatVariable,nameVariable,checkStudent=(5,12.3,"Erdo",False)
print(numberVariable)
print(floatVariable)
print(nameVariable)
print(checkStudent)

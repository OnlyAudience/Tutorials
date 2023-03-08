"""
Daire Alanı: Pi x r x r
Daire Çevresi: 2 x Pi x r
Pi = 3.14

Kullanıcıdan yarı çapı bilgisini alarak daire alanını ve çevresini hesaplayıp yazan bir program yazalım

>> Python Matematiksel Operatörler

+ Toplama
- Çıkarma
* Çarpma
/ Bölme
** Üs
% Mod
// Tam Bölme

"""

yariCap=float(input("Daire'nin yarı çapı uzunluğunu giriniz: "))

Pi=3.14
daireAlanı=Pi*(yariCap**2)
daireCevresi=2*Pi*yariCap

print("Daire Alanı: "+str(daireAlanı)+" Dairenin Çevresi: "+str(daireCevresi))
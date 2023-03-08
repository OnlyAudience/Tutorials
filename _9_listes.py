message='Merhaba, Ben Erdem'.split()
print(type(message))
print(message)

# Liste içerisine birbirinden farklı türlerde veri tanımlayabiliriz

listDiff=["Windows",12.5,True,3]
print(listDiff)

# String ifadelerini birleştirmek için kullandığımız + operatörü ile listeleri de birleştirebiliriz
list1=['one,','two']
list2=['three','four']
subList=list1+list2
print(subList)
print()

# Farklı liste birleştirme örnekleri
userA=['Sadık',36]
userB=['Çınar',27]

# + ifadesi ile iki listenin ögeleri ard arda yeni listeye kaydedilir.
usersList=userA+userB
print(usersList[0])

# Her listeyi tek bir liste olarak eklemek için de şu şekilde bir tanımlama yapabiliriz
usersList=[userA,userB]
print(usersList)
print(usersList[0][0])
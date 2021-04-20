
#KOŞULLU İFADELER
a = True
print(type(a))

bool(4)

# 5 > 3 true // 5 <3 false  // 5 ==3 false // 5!=3 true // "a" == "b" false //"a" < "z" true
#bool(0)sadece içi 0 olduğında false

#Mantıksal bağlaçlar
# and :  or - 1 durumun doğru olması

print(1<3)
#print(1<3 and 4<3) - her 2 durumun doğru olması
print(True and True)
print(True or False)

#print(2==2 and 4.5<2.6 and "asd" != "mdem")
print(not True)#sonucu değiştirme
print(not (4==4))

print(2==2 or 4.5<2.6 or "asd" != "mdem")

print(2==2 and 4.5<2.6 or "asd" != "mdem")
          #false   or    true >>> true

""" ***********************************************"""

#IF İfadeleri

a=4
b=5
c=6

if(a==3):
    print(a)
    print(b)

print("Merhaba")


yas=int(input("Yaşınızı girin : "))
if(yas>=20):
    print("dışarı çıkabilirsiniz")
else:
    print("dışarı çıkamazsınız")


sayi=int(input("Lütfen bir sayı giriniz : "))
if(sayi>=0):
     if(sayi % 2==0):
         print("girilen sayı çifttir.")
     else:
         print("girilen sayı tektir.")
else:
    print("sayı negatif")

    """ ***********************************************"""

#HESAP MAKİNESİ
a=45
b=34

secim=int(input("Toplama (1), Çıkarma(2),Çarpma(3),Bölme(4) \n İşlem Seçiniz : "))
if(secim==1):
    print(a+b)
elif(secim==2):
    print(a-b)
elif(secim==3):
    print(a*b)
elif(secim==4):
    print(a/b)
else:
    print("Hatalı Seçim")

""" ***********************************************"""

 #NOT TABLOSU
sonuc=float(input("Lütfen notunuzu giriniz : "))
if(sonuc >= 90):
    print("AA")
elif(sonuc >= 85):
    print("BA")
elif(sonuc >= 80):
    print("BB")
elif(sonuc >= 75):
    print("CB")
elif(sonuc >= 70):
    print("CC")
elif(sonuc >= 65):
    print("DC")
elif(sonuc >= 60):
    print("DD")
else:
    print("Kaldınız!")


""" ***********************************************"""

#Range fonk. > range(başlangıç değeri , bitiş değeri(dahil değil)
print(*range(0,10))
liste1= list(range(0,10))

print(*range(5,15))
print(*range(10))
print(*range(0,10,2))#2şer şekilde yazdırıyor 0 2 4 6 8

#print(*range(10,0)) - çalışmaz
print(*range(10,0,-1))#tersten 1 azalarak yazdırdı


for i in range(0,15):
    print(i)


 
for k in range(0,10):
    print("* "*k)

print("")
 
for k in range(10,0,-1):
    print("* "*k)

""" ***********************************************"""
#while
sayac=0
while(sayac<10):
    print(sayac)
    sayac +=1

sayac=0
while(sayac<10):
    print("Merhaba Dünya")
    sayac +=1

#sonsuz döngü
sayac=0
while(sayac<10):
    print(sayac) 

while(True):
    print("Sonsuz")

#breakContinue

sayac=0
while(sayac<10):
    print(sayac)
    if(sayac==5):#5i dahil etmek istemezsek printin üstüne
        break
    sayac +=1

print("")
sayac=0
while(sayac<10):
    print(sayac)
    if(sayac==5):
        continue
    sayac +=1


sayac=0
while(sayac<10):
   #5i görmezden geldi - 1 2 3 4 6 7 8 9 
    if(sayac==5):
        sayac +=1
        continue
    print(sayac)
    sayac +=1



 
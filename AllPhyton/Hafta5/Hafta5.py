#FONKSİYONLAR
#def FonksiyonAdi (par1,par2,....):
# fonksiyonunKodları

 


def karsilama(isim):
     print("Merhaba ben Siri , Hoşgeldin", isim)
     
karsilama("Yaren")

def karesiniAl(sayi):
    print(sayi*sayi)

karesiniAl(10)

def topla(sayi1,sayi2,sayi3):
    print("sonuç : ", sayi1+sayi2+sayi3)

topla(10,20,30)

def topla2(*sayilar):#* ile ist. kadar sayı girebilirim 
    toplam=0
    for i in sayilar:
        toplam+=i
        return toplam

print(topla2(1,2,3,5,4,5676,7))

""" ***********************************************"""

#Faktöriyel Hesaplama
def faktoriyel(sayi):
    sonuc=1
    for i in range(2,sayi+1):
        sonuc *=i
    print("Faktoriyel : " + sonuc)

faktoriyel(5)

""" ***********************************************"""
#ebob
def ebobBul(sayi1,sayi2):
    bolen=1#başlangıç değeri
    ebob=1
    while(bolen <= sayi1 and bolen <= sayi2):
        if((sayi1 % bolen == 0) and(sayi2 % bolen == 0 )):
            ebob=bolen
            bolen +=1
    return ebob

sayi1=int(input("sayi1 : "))
sayi2=int(input("sayi2 : "))

print("Ebob : " , ebobBul(sayi1,sayi2))

""" ***********************************************"""

#Mükemmel Sayı  
#1 sayının bölenleri toplamı kendisine eşitse 
#kendisi hariç

           
def muko(sayi):
    toplam = 0 

    for bolen in range(1,sayi):
        if(sayi % bolen == 0):
           toplam += bolen
    return toplam == sayi

for i in range(9999):
     if(muko(i)):
         print(i)

""" ***********************************************"""

#YEREL -GLOBAL DEĞİŞKENLER
a=10
def f1():
    global a  #artık her yerde 50
    a=50
    print(a)

f1()
print(a)#fonk. dışında 10 içinde 50


#Global örneği
def Menu():
    return input("(T)opla (F)ark (Y)azdir (C)ikis")

sayi1=0.
sayi2=0.0

sonuc=0.0
        
def sayiGir():
    global sayi1,sayi2
    sayi1=float(input("Sayi1 : "))
    sayi2=float(input("Sayi2 : "))

def Yazdir():
    print(sonuc)

def Topla():
    global sonuc
    sonuc=sayi1+sayi2
           
def Fark():
    global sonuc
    sonuc=sayi1-sayi2

def main():
    while True:
        secim = Menu()
        if secim == "T" or secim == "t":
            sayiGir()
            Topla()
            Yazdir()
        elif secim == "F" or secim == "f":
            sayiGir()
            Fark()
            Yazdir()
        elif secim == "Y" or secim == "y":
            Yazdir()
        elif secim == "C" or secim == "c":
          break

main()


""" ***********************************************"""
#LAMBDA: özet fonks.
def kupAl(n):
    return n**3
print(kupAl(5))

kupAl2 = lambda x : x**3
print(kupAl2(3))

toplaLambda  = lambda x,y,z : x+y+z
print(toplaLambda(2,4,5))


tersCevir = lambda s : s[::-1]
print(tersCevir("merhaba"))
print(tersCevir("1234567"))

""" ***********************************************"""
#2 basamaklı sag-yı
birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def okuma(sayi):
    birinvi=sayi%10#1.basamak
    ikinci=sayi//10#2.basamak
    return onlar[ikinci] +" " +birler[birinci]

sayi=int(input("Sayi : "))
print(okuma(sayi))
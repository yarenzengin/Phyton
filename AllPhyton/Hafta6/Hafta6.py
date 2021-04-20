
#Modul - kütüphane gibi

import math

dir(math)
#help(math) detaylı

print(math.factorial(5))
print(math.pow(5,6))
print(math.sqrt(81))

from math import* #tüm fonks. çağırır

print(factorial(4))

""" ***********************************************"""

class Araba():
    marka = "BMW"
    model = "i3"
    renk = "beyaz"
    kapiSayisi =4
    km=1000000

    def __init__(self):
        print("constructor çağrıldı")
    

#nesne oluşturma
araba1 = Araba()
print(type(araba1))

print(araba1.model)
print(Araba.marka)

""" ***********************************************"""

class Ogrenci():
    def __init__(self, ogrNo, isim,soyisim,bolum,dersler):
        self.ogrNo = ogrNo
        self.isim = isim
        self.soyisim = soyisim
        self.bolum = bolum
        self.dersler = dersler

    def bilgileriYazdir(self):
         print("""
         Öğrenci No : {}
         İsim : {}
         Soyisim: {}
         Bölümü:{}
         Dersleri:{}
            """.format(self.ogrNo,self.isim,self.soyisim,self.bolum,self.dersler) )

ogr1 = Ogrenci(1002,"yaren","zengin","YBS",["Mat1","NTP", "Phyton"])

print(ogr1.ogrNo)

ogr1.ogrNo = 987
print(ogr1.ogrNo)
print(ogr1.dersler)
   
ogr1.bilgileriYazdir()

""" ***********************************************"""

#KALITIM
class Personel():
    def __init__(self,isim,maas,sicilNo,departman):
        self.isim = isim
        self.maas = maas
        self.sicilNo = sicilNo
        self.departman = departman


    def BilgileriYazdir(self):
         print(" İsim : {}, Maaş: {}, Sicil No:{},Bölümü:{}".format(self.isim,self.maas,self.sicilNo,self.departman)) 


    def departmanDegistir(self,yeniDepartman):
      print("Departman değiştiriliyor")
      self.departman = yeniDepartman 

    def zamYap(self,zamMiktari):
        print("zam miktarı ekleniyor")
        self.maas += zamMiktari
    
p1 = Personel("Yaren",3000,1003,"İK")
p1.BilgileriYazdir()
p1.departmanDegistir("muhasebe")
p1.zamYap(500)
p1.BilgileriYazdir()

class Yonetici(Personel):
    def __init__(self, isim, maas, sicilNo, departman,kisiSayisi):
        super().__init__(isim,maas,sicilNo, departman)
        self.kisiSayisi = kisiSayisi

    def BilgileriYazdir(self):
         print(" İsim : {}, Maaş: {}, Sicil No:{},Bölümü:{}, Sorumlu olduğu kişi sayısı : {}".format(self.isim,self.maas,self.sicilNo,self.departman,self.kisiSayisi)) 

y1 = Yonetici("Yaren Zengin",10000,12,"İK",25)
y1.BilgileriYazdir()

   
       

  

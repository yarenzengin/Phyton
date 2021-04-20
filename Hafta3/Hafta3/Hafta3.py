
#DEĞİŞKENLER
"""
çoklu yorum satırı
"""

"""
 Değişken isimleri
 *sayı ile başlayamaz
 *kelimeler arası boşluk olmaz
 * : "",<> !() @$ kullanılamaz  _ kullanılabilir
 *kodlamaya özel kelimeler (while ,def,true vb ) kullanılamaz
"""

#PRINT FONKSİYONU
print(45)
print(14.4)

a=15
b=20
print(a+b)

print("********************* 1 ******************************** ")
print("Merhaba Dünya")
print("Merhaba" , 12,13,1)
print("Merhaba", "Dünya")
print("Merhaba\nSınıf\nNasılsınız?")#enter
print("""Merhaba
Sınıf 
Nasılsınız

""") # 3 tırnak özelliği 
print("Merhaba \tDünya") #tab 

print("********************* 2 ******************************** ")
#TYPE FONKSİYONU > herhangi bir değişkenin tipini öğrenebilmek için kullanıyoruz
a=55
print(type(a))

b=5.45
print(type(b))

print("********************* 3 ******************************** ")
#sep parametresi
print(1,2,3) #boşluklu yazıyor
print(1,2,3,sep=".")#arasına nokta koyarak yazıyor
print(17,3,2021,sep="/")
print(1,2,3,sep=",")
print("Ocak","Şubat","Mart",sep="\n")

print(*"Yaren") # her karakterin arasına boşluk atar
print(*"Yaren",sep="\n") 

print("********************* 4 ******************************** ")
#formatlama
x=3
y=5

print("{} + {} 'nın toplamı {} dır.".format(x,y,x+y))#{}>değişken yazacağım anlamına geliyor
print("{} {} {}".format(17,3,2021))#format ile değer verebiliyoruz
print("{1} {0} {2}".format(17,3,2021))#değerlerin sırası değişti

print("{:.4f} {:.3f} {:.2f}".format(1.47837,3.3948324,2.3029420))
#4 hassasiyetle yazdır, 3 hassa. yazdır, 2 hass.le yazzdır >> 1) 1.4790 2)3.3400 3 )2.30 >> yuvarladı

print("********************* 5 ******************************** ")
#LİSTELER#dizilere benziyor

liste = [1,2,3,4,5]
print(liste)

liste2 = ["a","b","c"]
print(liste2)

liste3= ["merhaba"," dünya"]
print(liste3)

liste4 = [1,2,3,"a", 4,5, "kitap",33.45]
print(liste4)

print("********************* 6 ******************************** ")
#boş liste
bos_liste = []
bos_liste2 = list()

#liste boyutu, eleman
print(len(liste))
print(len(liste4))

s="yaren"
liste5 = list(s)#stringin her bir harfini diziye karakter ol.alabiliyor
print(liste5)

print("********************* 7 ******************************** ")

#elemanlarına ulaşmak için
liste = [1,2,3,4,5]
print(liste[0])
print(liste[4])
#print(liste[6])#hata> list index out of range

#son elemana ulaşma
print(liste[-1])
print(liste[len(liste)-1])
#ilk elemana ulaşma
print(liste[0])
print(liste[-len(liste)])

print("********************* 8 ******************************** ")

print(liste[:3])#3.indexe kadar getirdi . 3 dahil değil
print(liste2[:2])

liste6 = [1,2,3,4,5,6,7,8,9]
print(liste6[::2]) #2'şer git 1,3,5,7,9
print(liste6[::-1])#tersten yazdı

print("********************* 9 ******************************** ")
#Liste İşlemleri 
liste7 = liste + liste2
print(liste7)

liste = liste + [6]
liste2 = liste2 + ["d"]#yeni eleman ekleme

liste[0] = 0 #0. indexsin yeni değeri 0 oldu 

print(liste*3)#3 defa yazdırıyor

liste = liste * 2 #boyutu değişti

print("********************* 10 ******************************** ")
#append komutu
liste1=[0,1,2,3]
liste1.append(4)#yeni eleman ekleme
liste1.reverse()
print("********************* 11 ******************************** ")
#pop komutu
#liste1.pop()#son elemanı listedenatar
liste1.pop(0)
print("********************* 12 ******************************** ")
#sort komutu > sıralamaya yarıyor
liste.sort() #küçükten büyüğe
liste.sort(reverse =True) #büyükten küçüğe

liste2.sort(reverse =True)

#İç içe listeler
print("********************* 13 ******************************** ")

l1=[1,2,3]
l2=[4,5,6]
l3=[7,8,9]

listeb =[l1,l2,l3]#2köşeli parantez iç içe
print(listeb)
print(listeb[1][0]) #4 > elemana ulaştı
print(listeb[2][1])


print("********************* 14 ******************************** ")
#DEMETLER - TUPLE , listeden farkı değiştirilemez
demet = (1,2,3,4)
print(type(demet))

print(demet[0]) #0. elemana ulaştı
print(demet[1:3]) #2,3

#demet metotları

demet2 = (1,2,3,"M")
print(demet2.index(3))#elemanın indexi
print(demet2.index("M"))

demet3= (1,1,1,2,2,3,3,3)
print(demet3.count(1))#1 elemanından kaç tane var
print(demet3.count(12))#böyle bir eleman yok hata değil 0 Verir

#demet [0] = 0 #hata

print("********************* 15 ******************************** ")
#SÖZLÜK - DICTIONARY
sozluk = {"book":"kitap","apple":"elma"}
print(sozluk)
print(type(sozluk))

bos_sozluk = {}
bos_sozluk2 = dict()

sozluk2 = {"bir":1, "iki":2}
print(sozluk2["bir"])#> 1
print(sozluk2["iki"])#> 2

#eleman ekleme
sozluk2["dort"]=4
print(sozluk2.keys())#yazı ile olan kısmı getiriyor
print(sozluk2.values())#verd. değeri getirdi

#iç içe sözlükler
s3={"aylar":{"ocak":1,"şubat":2,"mart":3},"sayilar":{"bir":1,"iki":2}}
print(s3["aylar"]["mart"])#3



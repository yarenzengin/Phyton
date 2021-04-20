

#SAYILAR---shift+enter
a=43
b=5.0
float(a)
a
print(a)

print(float(85))
print(int(4.5))
print(int(4.9))
print(int(a/b))
#stringe çevirme
a=7363
b=str(a)
print(b)

len(b)#uzunluğunu  aldk

c=45.78#leni floatta kullanamazzsın
d=str(c)
print(d)
len(d)
#stringleri sayıya çevirme
a="8810"
b=int(a)
print(b)

#stringleri ondalıklı sayıya çevirme
a="91.91"
b=float(a)
print(b)

#Hatalı olanlar
#c="939.3ıjdssd"
#d=float(c)

#c="cksjcksd"
#d=int(c)

#MATEMATİKSEL OPERATÖRLER
x=23
y=5
z=12
print(x+y)
print(x-y)
print(x+y+z)
print(x*y)
print(4/2)#çıktısı her zaman float şeklinde
print(x/y)
#Tam Bölme
print(4//2)
print(89//5)
#Mod
print(18%5)
print(15%5)
#Kuvvetini alma
print(2**8)
print(10**2)
#karekök > 
print(25**0.5)


i=90.7
j=6.5
print(i+j)
print(j-i)

#İşaret değiştirme
z=789
print(-z)#neg.

print(9+5//1-3*2)


#STRINGLER
print("Merhaba Dünya")
print('Merhaba Dünya')
print("""Merhaba Dünya""")

print("Bandırma'da hava çok güzel")#kesme işareti kullanıcaksan çift tırnak olarak kullan

isim="yaren"
print(isim)

isim[0]#karaktere ulaşıyoruz , kendisi paarçalıyor
isim[-1]#en sonuncu karakter için
isim[4]
isim[-2]

a="Phyton Proglama"
a[:10]# a'yı seçtik ve ilk 10 karakteri aldık
a[10]#tek bir karakter
a[6:]#6.karakterden sonrası
a[2:11]#2.ile 11. karakter arası
a[:-1]#baştan başlicak en sona kadar gidecek
a[:]#tüm ifadeleri yazdırır.


a[::2]#2şer arttırarak yazdır
a[2:12:3]#2den 12 ye ama 3 er atlayarak
a[::-1]#tersten yazdır

len(a)
#string birleştirme

x="Merhaba "
y="Dünya"
x+y
x*5#Merhabayı 5 defa yazdırır
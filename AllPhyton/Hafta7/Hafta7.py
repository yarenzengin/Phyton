#HATALAR
#print(sayi) > NAME ERROR değişken tanımlanmadı

#sayi1 = int ("1,2,3asd") > VALUE ERROR değerde hata var
#sayi3 = 5/0 > ZeroDivisionError

#print("merhaba"dünya) > SyntaxError


#HATA AYIKLAMA
try:
    sayi1=int("1,2,3asd")
    print("try bloğu içerisinde")

except ValueError:
    print("hata oluştu")#direkt exceptiona geçiyor

print("try bloğu dışı")

try:
    sayi2= 5/0

except ZeroDivisionError:
    print("sıfıra bölünme hatası")

""" ***********************************************"""

try:
    sayi3 = int(input("sayi1: "))
    sayi4 = int(input("sayi2: "))
    print(sayi3/sayi4)

except ValueError:
    print("lütfen sadece rakam giriniz")

except ZeroDivisionError:
    print("sayı 2  0 olamaz")

finally:
    print("Finally bloğu her zaman çalışır")


""" ***********************************************"""


def terstenYazdir(metin):
    if(type(metin) != str):
        raise ValueError("sadece string değerler olmalı")
    else:
        return metin[::-1]

print(terstenYazdir("yaren"))

try:
    print(terstenYazdir(50))
except ValueError:
    print("hata oluştu")


                                                                                



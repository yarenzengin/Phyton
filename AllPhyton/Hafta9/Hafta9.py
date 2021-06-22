
#Özel Kütüphane- NumPY
#dosyanın başında import etmemiz gerekiyor 
#1,2,3d array >> tipini  belirleyebiliyoryz
#şablon olarak tsarlamak istiyorsak > zeros 
#spesifik veriler de verebiliyoruz

#
a=[1,2,4, "merhaba"]
b=[5,6,7]

ab=[]

for i in range(0,len(a)):
    ab.append(a[i]*b[i])

print(ab)

import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a*b)

print(type(a))

print(np.array([1,2.5,3.6,5],dtype="int"))
#sıfırdan array oluşturma
print(np.full((3,5),5))

np.zeros(4)#0 lardan oluşan bir matris > varsayılan tip float
np.zeros((2,3),dtype="int")

np.ones((2,3),dtype="int")

np.arrange(0,21,2)#çift sauıları aaldı

np.linspace(0,1,10)#10 parçaya böldü

np.random.normal(10,5,(4,5))#4 satır 5 sütundan oluşan bir matris oluşturduk 
#ortalaması(loc) 10 olan standart sapması 5 olan

m=np.random.randint(0,100,(2,3))#0 ile 100 arasında bir matris

m.ndim # boyutunu verdi
m.shape # satır,sütun bilgisi verir
m.size # veri sayısı
m.dtype # türünü verir

#RESHAPPING - MATRİSİN BOYUTUNU DEĞİŞTİRME
n= np.arange(1,10)
n.ndim

n.reshape((3,3))#boyutu uymuyorsa hata verir > cannot reshape array of size 11 into shape 3,3
n.ndim#şekilsel anlamda bir değişiklik yaptı tutmak istiyorsak bir listeye atmalıyız 

k=n.reshape((3,3))
k.ndim

#Array Birleştirme

x=np.array([1,2,3])
y=np.array([4,5,6])

np.concatenate([x,y],axis=0)#  1 2 3 4 5 6

z=np.array([7,8,9])
np.concatenate([x,y,z])

#2 boyutta birleştirme
a=np.array([[1,2,3],[4,5,6]])
a.ndim

np.concatenate([a,a])  # satır bazında birleştirdi
a1=np.concatenate([a,a],axis=0)  # satır bazında birleştirdi
a1.shape # (4,3) satır bazında old .için 2 den 4 e çıktı
np.concatenate([a,a],axis=1)  # sütun bazında birleştirdi > 1,2,3,1,2,3\n4,5,6,4,5,6 > shape = 2,6

# 2 boyutlu arraylerde ayırma
l= np.arange(16).reshape(4,4)

np.vsplit(l,2) # l yi satır bazında 2 ye böldü 

ust,alt= np.vsplit(l,2)
ust
alt #matris

np.hsplit(l,2) # dikey ol. sütun bazında 
sol,sag = np.hsplit(l,2)
sol
sag
#sol > 0 1 ,4  5, 8 9,12 13
#sağ > 2 3 ,6 7, 10 11,14 15
#array sıralama işlemleri(sorting)
import numpy as np

v = np.array([4,8,9,2,3,5,1])

np.sort(v) #geçici sıralama
v

v.sort() # kalıcı sıralama

##2 boyutlu arraylerde sıralama 

m=np.random.normal(15,3,(3,3))
m

np.sort(m,axis=1)#satır
np.sort(m,axis=0)#sütun

#index
a=np.random.randint(10,size=10)
a

a[0]
a[-1]
a[0]=55#güncelleme

#2 boyutlu arraylerde indexleme
m=np.random.randint(10,size=(3,4))
m
m[0,0] #ilk eleman
m[2,1] #2 satır değeri 1 sütun değeri
m[2,2] =9
m

#satır,sütun

#slicing
c=np.arange(10,20)
c

c[0:3]
c[3:]
c[1::2]

#2 boyutlu

n=np.random.randint(10,size=(5,5))
n
#sütun
n[:,0]#ilk sütunu getirdi
n[:,1]
n[:,5] #hatalı

#satır
n
n[0,:]

n[1:2,0:3] #1.satır ve 0,1,2. sütundaki elemanlar gelir

#Koşullu eleman işlemleri
v=np.array([3,-5,6,7,8,11])
v<7# t f ol. geliyor

v[v<7]#değerleri getiriyo
v[v>7]
v[v<=7]
v[v>=7]
v[v==7]
v[v!=7]
#matematiksel işlemler
v*2
v/3
v*4/5
v**2#tüm değerlerin karesini aldı

np.subtract(v,1)#tüm elemanlardan 1 çıkarıyor
np.add(v,1) #toplama
np.multiply(v,2) #çarpma
np.divide(v,3) #bölme

np.power(v,2)#karesini alma
np.mod(v,2)#mod alma
np.absolute(v) #mutlak değerli hali

np.sin(180)
np.cos(0)

np.log(v)
np.log10(v)

#istatiksel hesaplama
x=np.array([3,5,7,9])
np.mean(v)#ortalama

x.max() #max değeri getirir
x.min()
x.sum()#toplamları

np.std(x)#standart sapma
np.var(x)#varyans

#2 bilinmeyenli denklem çözüm

 #5*x+1*y = 12
 #1*x + 3*y =10

a=np.array([[5,1],[1,3]]) # katsayılarını vermek gerekiyor
b=np.array([12,10])

c=np.linalg.solve(a,b)#matrise aktardık
c


import matplotlib.pyplot as plt 
import numpy as np
#print(matplotlib.__version__) 

x=np.array([0,6])#başlangıç ve bitiş değeri

y=np.array([0,51])

plt.plot(x,y)#grafik oluşturdu
plt.plot(x,y,'o') #çizginin başlangıç ve bitiş noktası
plt.show()

x2=np.array([1,2,5,8])
y2=np.array([3,5,9,11])

plt.plot(x2,y2)


y3=np.array([2,3,1,6,4])
plt.plot(y3)# x i default alıyor

#nokta(ilk gird.ifade ),çizgi , renk
#nokta çeşitleri
plt.plot(y3,marker='o')#noktaları yuvarlak şeklinde koyduk
plt.plot(y3,marker='*')
plt.plot(y3,marker='+')
plt.plot(y3,marker='.')
plt.plot(y3,marker=',')
plt.plot(y3,marker='x')
plt.plot(y3,marker='P')
plt.plot(y3,marker='d')
plt.plot(y3,marker='D')
plt.plot(y3,marker='p')
plt.plot(y3,marker='h')
plt.plot(y3,marker='H')
plt.plot(y3,marker='<')
plt.plot(y3,marker='>')
plt.plot(y3,marker='|')
plt.plot(y3,marker='_')

#çizgi çeşitleri
plt.plot(y3,'o-')
plt.plot(y3,'o--')
plt.plot(y3,'o:')
plt.plot(y3,'o-.')

#renk çeşitleri
#r,g,b,c,m,y,k,,w
plt.plot(y3,'o-.r')
plt.plot(y3,'o-.c')
plt.plot(y3,'*:m')

plt.plot(y3,'*:m',ms=20) #ms = marker size işareti büyüttük

#marker edge color/ işaretçi kenar rengi
plt.plot(y3,'o:y',ms=20,mec='r')#noktalarıni çi safrı dışındaki çizgiler kırmızı

#marker rengi/ mfc
plt.plot(y3,'o:y',ms=20,mfc='r')
#hem çerçeve hem işarertçi rengini değiştirme
plt.plot(y3,'o:y',ms=20,mec='r',mfc='r')

#hexamdeical renk modu 
plt.plot(y3,'o:y',ms=20,mec='#217D33',mfc='#217D33')


#sadece  çizgileri görmek istiyorum

plt.plot(y3,linestyle='dotted') #noktalar ile
plt.plot(y3,linestyle='dashed')#çizgiler ile
plt.plot(y3,ls=':') 

plt.plot(y3,color = 'r')#çizginin rengi
plt.plot(y3,color='hotpink') 

plt.plot(y3,linewidth='10') #çizginin boyutu


#çoklu çizgiler
#y eksenine göre çizebilsin diye ikisinde y verdik 
y1=np.array([1,2,5,8])
y2=np.array([3,5,9,11])

plt.plot(y1)
plt.plot(y2)

plt.show()


x1=np.array([0,1,2,3])
y1=np.array([2,4,6,8])
x2=np.array([0,1,2,3])
y2=np.array([1,3,5,7])
plt.plot(x1,y1,x2,y2)


#eksen isimleri
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")

#başlık
plt.title("Başlık")

plt.grid()#arka plan ızgara şeklinde

plt.grid(axis='x')#sadece dikey çizgileri aldı
plt.grid(axis='y')#sadece yatay çizgileri aldı

plt.grid(color='g',linestyle= ':',linewidth=0.5)

#aynı anda 2 veya 4 grafiği nasıl gösteririz
x1=np.array([0,1,2,3])
y1=np.array([2,4,6,8])
plt.subplot(1,2,1)#alt çerçeve
plt.plot(x1,y1)


x2=np.array([0,1,2,3])
y2=np.array([1,3,5,7])
plt.subplot(2,1,2)
plt.plot(x2,y2)


plt.scatter(x1,y1)#sadece noktalardan oluşuyor
plt.scatter(x2,y2)

plt.bar(x1,y1)#sütun olarak

plt.barh(x2,y2)# x ekseninde görmek istersen


x=np.random.normal(10,20,200)

plt.hist(x)

y1=np.array([2,4,6,8])
plt.pie(y)#pasta grafik
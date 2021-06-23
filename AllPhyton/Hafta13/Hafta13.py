from turtle import * 
#özel bir şekil çizmek istiyosan


t=turtle.Turtle()
t.forward(100)# 100 birimlik ileri çizgi çiz > sağa doğru çizdi
t.left(90)#90 derece sola dön 
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)



turtle.done()

#for döngüsü ile 
for i in range (4):
    t.left(90)
    t.forward(100)

turtle.done


#fonks. ile yapma

def kareCiz():
    for i in range (4):
        t.forward(100)
        t.left(90)
       

kareCiz()

def kareCiz(birim):
    for i in range (4): # kenardan oluştuğu için
        t.forward(birim)
        t.left(90)
 
# 4 tane iç içe kare oldu         
kareCiz(50)    
kareCiz(100)    
kareCiz(150)    
kareCiz(200) 

#çokgen çizdirme
def sekilCiz(kenarSayisi):
    disAci=360/kenarSayisi
    for i in range(kenarSayisi):
        t.forward(100)
        t.left(disAci)

sekilCiz(3)
t.clear()#sayfayı temizledik
sekilCiz(4)
t.clear()
sekilCiz(5)
t.clear()
sekilCiz(6)
t.clear()
sekilCiz(12)
t.clear()



t.pensize(5)#kalem kalınlığı
t.color("red", "black") # 1.ifade çizginin rengi , 2.ifade dolgunun
t.begin_fill()
t.circle(100) #daire
t.end_fill()#doldurma işlemini yaptı

#merdiven çizimi
def merdiven(basamakSayisi,uzunluk):
    t.speed(1)
    t.penup()#kalemi kaldır
    t.goto(-200,-200)#gitmek ist. konum
    t.pendown#kalemi koy 
    for i in range(basamakSayisi):
        t.forward(uzunluk)
        t.left(90)
        t.forward(uzunluk)
        t.right(90)


merdiven(6,50)
t.clear()
merdiven(10,10)
t.clear()
merdiven(3,150)
t.clear()
turtle.done()


#TIME ÖRNEKLERİ

from time import * 


#sleep > prog. çalıştırıldığında belirtilen süre kadar durmasını sağlar?
for i in range(10,0,-1):
    print(i)
    sleep(1)#sn olarak

print("Bir seyler yaziniz")
baslangic = clock()
yazi= input("sureniz basladi")
bitis=clock()#saati açtı?
sure=bitis-baslangic
print(sure)

print(strftime("%c"))#gün ay saat yıl verdi  # bunun içine yazdığın özel karakterlerle nasıl çaloşmasını gerektiğini söylüyorsun
print(strftime("%x")) # sadece tarihi verdi
print(strftime("%j"))#yılın kaçıncı günündeyiz
print(strftime("%U" )#yılın kaçıncı haftasındayız

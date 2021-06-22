
#DOSYALAMA İŞLEMLERİ 
#dosya açmak için open metodunu kullanıcaz bunun için de dosya adı ve modu gerekiyor
#r > read , a > append , w> write , c > create
#  modu  text (t) mi olucak binary (b) mi belirleyebiliriz
#f =  open("demofile.txt"): dosya kodu kaydettiğin klasördeyse böyle yazmak yeterli yoksa dosya yolunu belirtmek gerekiyor
# "rt"  > read and text 

#f = open("demofile.txt","r")
#print(f.read())-satırı okumak için readline
#close ile kapatmalyız ya da with komutu var aç benim işimi gör kendi kendine kapat
# w komutu biraz tehlikeli çünkü içindeki şeyleri silip ekleyebiliyor
#remove silme

print("**************************************")

#DOSYA AÇMA
f =  open("1.txt","w")
f.close()

f2 = open("C:\\Users\\Yaren\\Desktop\\3.txt","w")
#ya da normal / kullan  hata almamak iöin
f2.close()

f =  open("1.txt","w") #içindeki yazıyı siler
f.write("merhaba dünya")
f.close()

f =  open("1.txt","a") #içinde yazandan devam eder
f.write("merhaba dünya 2\n")
f.close()

#DOSYA OKUMA


#file.close()

try:
    file = open("C:\\Users\\Yaren\\Desktop\\4.txt", "r")
except FileNotFoundError: 
    print("dosya bulunamadı")


file = open("C:/Users/Yaren/Desktop/3.txt", "r")
for i in file:
    print(i,end="")#satır aralarına enter atmasın diye
file.close()

file = open("C:/Users/Yaren/Desktop/3.txt", "r")
print(file.read())
file.close()

file = open("C:/Users/Yaren/Desktop/3.txt", "r")
print(file.readline())#tek bir satır okuyor
print(file.readlines()) #ile listeye atıyor ve tüm satırları okuyor
file.close()

with open("C:/Users/Yaren/Desktop/3.txt", "r") as file:
    for i in file:
        print(i)

#seek , tell : 
with open("C:/Users/Yaren/Desktop/3.txt", "r", encoding="utf-8") as file:
        file.seek(5)#kaçıncı byte da olduğunu saydı
        print(file.tell())#imleç nerede
        k=file.read(10)
        print(file.tell())


#dosyanın 5.byte ından sonra yazma
with open("C:/Users/Yaren/Desktop/3.txt", "r+", encoding="utf-8") as file:
        file.seek(5)
        file.write("deneme")

#dosyanın sonuna yazma
with open("C:/Users/Yaren/Desktop/3.txt","a", encoding="utf-8") as file:
        file.seek(5)
        file.write("satır 4\n ")

#dosyanın başına yazma
with open("C:/Users/Yaren/Desktop/3.txt", "r+", encoding="utf-8") as file:
    icerik= file.read() 
    icerik = "satır 0\n" + icerik
    file.seek(0)
    file.write(icerik)



#
def sicaklik(satir):
    satir=satir[:-1]
    liste2 = satir.split(",")
    sehirIsmi= liste2[0]
    minSicaklik=int(liste2[1])
    maxSicaklik=int(liste2[2])
    ortSicaklik=(minSicaklik+maxSicaklik)/2
    if(ortSicaklik >= 15):
        durum = "sıcak"
    elif(ortSicaklik >=5):
        durum = "ılık"
    else:
        durum = "soğuk"
    return sehirIsmi +" "+ durum + "\n"




with open("C:/Users/Yaren/Desktop/3.txt","r") as file:


    liste=[]
    for i in file:
        liste.append(sicaklik(i))

print(liste)

#PANDAS KÜTÜPHANESİ
#veriler hem kategorik hem sürekli ol.verilebiliyor özellikle grafik..
#npy da indexlere erişemiyoduk pandasta indexleri  değiştirebiliyrouz adlandırabiliyoruz
#2 boyutlu old. için dataframe oluşturuyoruz
#
#
#
import pandas as pd

df=pd.DataFrame({'siniflar':['A','B','C','B','A'],'sinavlar':[35,45,85,55,75]},column=['siniflar','sinavlar'])

df

df.groupby("siniflar").sum()#gruplayıp topladık

df.groupby("siniflar").mean()#ortalama


import seaborn as sns

df=sns.load_dataset("planets")


df.head() #sayısal mı değil mi kategorik mi değil mi diye tespit ettik, İLK 5 deüeri getirdi
df.tail()#son 5 değeri getirdi
df.info()#tipiyle ilgili bilgi verecektir



df.groupby("method").mean() #metota göre sırala ve ort. al

#1 sütundaki verilerin ort.
df.groupby("method")["orbital_period"].mean()

df.describe()#tanımlayıcı verileri verio> ort.,standart sapma ...
a=df.groupby("method")["orbital_period"].describe() #istatiksel verilere ulaşabiliriz


s=[10,15,25,35] #bunu nasıl pandas serisine çeviricez

 seri = pd.Series(s)
 seri

 #serilerin indexleri
 seri[0]
 seri[3]
 seri[5]#hatalı

 #indexlerini nasıl değiştirebiliriz
 seri2=pd.Series(s,index=["x","y","z","t"])

 seri2["z"]#değeri 25


 #sözlük
 sayilar={"bir":1,"iki":2,"üç":3}

 seri3=pd.Series(sayilar,index=["bir","iki"])#dataframeleri oluştururken böyle sözlükleri de kullanabilirsin
 seri3


 #2 boyutlu 
 df2=pd.DataFrame({'siniflar':['A','B','C','B','A'],'sinavlar':[35,45,85,55,75]},column=['siniflar','sinavlar'])

 df2
 df2.loc[1]#indexi 1 olan satır değerini getirir

 df2.loc[[2,3]]


 #veri silme , yanlış girilmiş veya çoğaltılmış verileri temizlemek gerekir
 df

 #boş verileri temizleme

 yeni_df=df.dropna()
 yeni_df.info()

 #boş veriler yerine değer girme

 yeni_df2=df.fillna(0)

 df.head()
 #ortalamasını alıp boş verilere vericez

 o_ort=df["orbital_period"].mean()
 o_ort
 df.describe()

 yeni_df3 = df
 yeni_df3=["orbital_period"].fillna(o_ort,inplace=True)
 yeni_df3.describe()

 #eğer aynı veriler varsa silme

 d=df.duplicated()
 df.drop_duplicates(inplace=True)




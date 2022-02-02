# 1-Bmw,Mercedes,Opel,Mazda,Volvo elemanlarına sahip liste oluşturunuz.
cars=["Bmw","Mercedes","Opel,","Mazda","Volvo"]
print(cars)

# 2-listenin ilk ve son elemanı nedir
print(cars[0])
print(cars[-1])

# 3-liste kaç elemanlı
print(len(cars))  

# 4-Mazda değerini Toyota ile değiştiriniz
cars[-2]="Toyota"
print(cars)

# 5-Mercedes listenin bir elemanı mı?
result="Mercedes" in cars
print(result)

# 6-Listenin -2 indeksindeki değer nedir?
print(cars[-2])

# 7-Listenin ilk üç elemanını alınız.
print(cars[0:3])

# 8-Listenin son iki elemanı yerine "Honda" ve "Audi"
cars[-2:]=["Honda","Audi"]
print(cars)

# 9-Listenin üzerine "Volvo" ve"Nissan değerlerini ekleyin
result=cars + ["Volvo","Nissan"]
result=cars
print(result)

# 10-Listenin son elemannı silin..
del cars[-1]
result=cars
print(result)

# 11-Liste elemanlarını tersten yazdırın.
result=cars[::-1]
print(result)

# 12-Aşağıdaki verileri bir liste içinde saklayınız...
       #studentA: Yiğit Bilgi 2010, (70,60,70)
       #studentB: Sena Turan 1999,  (80,80,70)
       #studentC: Ahmet Turan 1998, (80,70,90)
       
studentA=["Yiğit","Bilgi",2010,[70,60,70]]
studentB=["Sena","Turan",1999,[80,80,70]]
studentC=["Ahmet","Turan",1998,[80,70,90]] 

print(studentB[3][2])      
       
       




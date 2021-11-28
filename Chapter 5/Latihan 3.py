angka = 0
count = 0
hasil = 0
while(angka <= 100):
    if(angka % 2 == 1):
        count += 1
        hasil += angka
        print(angka)
    angka += 1
print("\nBanyaknya bilangan ganjil :",count)
print("Jumlah seluruh bilangan :",hasil)
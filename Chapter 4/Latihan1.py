import time

def jam(jampinjam, jamkembali) :
    return jamkembali-jampinjam
def menit(menitpinjam, menitkembali) :
    return menitkembali-menitpinjam
def keseluruhan(lamajam, lamamenit) :
    return lamajam*60+lamamenit

print("----Rental Mobil Jiwa Agung----")

print("Tarif sewa Rp 200.000 untuk 12 jam pertama dan untuk berikutnya adalah Rp 10.000/jam")
time.sleep(3)

print("Waktu peminjaman")
jampinjam = int(input("Jam : "))
menitpinjam = int(input("Menit : "))
print("Waktu pengembalian")
jamkembali = int(input("Jam : "))
menitkembali = int(input("Menit : "))
lamajam = jam(jampinjam, jamkembali)
lamamenit = menit(menitpinjam, menitkembali)
print("Lama peminjaman = ", lamajam, "Jam", lamamenit, "Menit")
total = keseluruhan(lamajam, lamamenit)
print("Lama peminjaman dalam menit = ", total, "menit")
if total<721:
    print("Maka total harga yang harus dibayar = Rp 200.000")
elif total>720:
    Total = int((total-720)*166.6666666666667+200000)
    print("Maka total harga yang harus dibayar = Rp ", Total)


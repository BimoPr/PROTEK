print("----Lama Perjalanan----")

def akeb(jarakakeb, kecepatanakeb) :
    return (jarakakeb*1000)/(kecepatanakeb*1000/60)
def bkec(jarakbkec, kecepatanbkec) :
    return (jarakbkec*1000)/(kecepatanbkec*1000/60)
def total(total1, total2, istirahat) :
    return (total1+total2+istirahat)

jarakakeb = float(input("Jarak dari kota A ke kota B : "))
kecepatanakeb = float(input("Kecepatan rata-ratanya : "))
total1 = round(akeb(jarakakeb, kecepatanakeb))
print("Waktu yang dibutuhkan dari kota A ke kota B adalah", total1, "menit")
print("_____________________")
jarakbkec = float(input("Jarak dari kota B ke kota C : "))
kecepatanbkec = float(input("Kecepatan rata-ratanya : "))
total2 = round(bkec(jarakbkec, kecepatanbkec))
print("Waktu yang dibutuhkan dari kota B ke kota C adalah", total2, "menit")
print("_____________________")
istirahat = float(input("Lama waktu istirahat : "))
totalwaktu = round(total(total1, total2, istirahat))
print("Maka total waktunya", totalwaktu, "menit")
print("_____________________")
total = round(total(total1, total2, istirahat))
Jam = round(total/60)
Menit = total-Jam*60
print("Lama Perjalanan adalah",(Jam), "jam",(Menit), "menit")
print("_____________________")
#menghitung total keseleluruhan waktu
print("Waktu berangkat pukul : ")
jam = float(input("Jam : "))
menit = float(input("Menit : "))
jamsampai = jam+Jam
menitsampai = menit+Menit
print("_____________________")
if (menitsampai < 60):
    print("tiba pukul",(jamsampai)," : ",(menitsampai))
elif(menitsampai > 60):
    jm = jamsampai+1
    mnt = menitsampai-60
    print("tiba pukul",(jm)," : ",(mnt))


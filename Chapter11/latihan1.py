from datetime import *
datee = datetime.date(datetime.now())
try:
    datenput = input("Masukkan tanggal yang ingin dicari(YYYY-MM-DD):")
    a = datenput.split("-")
    dateor = date(int(a[0]), int(a[1]), int(a[2]))


    def diffdate(x):
        datechange = datee - x
        return datechange.days


    print('Selisih hari dari tanggal yang terinput adalah', diffdate(dateor), 'hari')
except ValueError:
    print('Maaf Input Tidak Valid')
from datetime import *

file = open("latihan3e.txt", "r")

data = file.readlines()

data1 = []

def diffDate():
    global datee
    global datex
    datee = datetime.date(datetime.now())
    datex = date(2021, 12, 4)
    dateall = datee - datex
    return dateall.days

price = diffDate() * 2000
borw = date(2021, 11, 28)

for i in range(len(data)):
    fix = data[i].replace('\n', '') 
    split = fix.split("|")
    Dict = {"code": split[0], "name": split[1], "title": split[2]}
    data1.append(Dict)

while True:
    find = input('Masukkan NIM yang ingin dicari : ')

    for i in range(len(data1)):
        if find in data1[i]['code']:
            print('-------------------------------')
            print('Data Peminjaman Buku')
            print('Kode Member              : ', str(data1[i]['code']))
            print('Nama Member              : ', str(data1[i]['name']))
            print('Judul Buku               : ', str(data1[i]['title']))
            print('Tanggal Mulai Peminjaman : ', borw)
            print('Tanggal Maks Peminjaman  : ', datex)
            print('Tanggal Pengembalian     : ', datee)
            print('Terlambat                : ', diffDate())
            print('Denda                    : ', price)
            print('-------------------------------')

        if find not in data1[0]['code']:
            if find not in data1[1]['code']:
                if find not in data1[2]['code']:
                    print("\"Data mahasiswa tidak ditemukan\"")
    
    
    try2 = input('Ingin mengulangi (y/n)?')
    if try2 in ('N', 'n'):
        break

file.close()
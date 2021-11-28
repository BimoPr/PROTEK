buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
jumlah = 0

try:
    def data():
        print('Nama buah yang ingin dibeli : ', end='')
        nama = input()
        print('Berapa KG                   : ', end='')
        banyak = int(input())
        global hasil
        hasil = banyak * buah[nama]
        global jumlah
        jumlah += hasil
        global ans
        ans = input("Beli buah lainnya (y/n)? ")

    while True:
        print('Menu:')
        print('A. Tambah Data')
        print('B. Beli Buah')
        pilihan = input('Pilihan Menu = ')
        if pilihan in ('A', 'a'):
            print('Masukkan nama buah : ', end='')
            tambah = input()
            if tambah in buah.keys():
                print("Nama buah sudah ada didalam dictionary")
            else:
                print('Masukkan harga satuan : ', end='')
                harga = int(input())
                buah[tambah] = harga
                print('Data buah :')
                for key, value in buah.items():
                    print('- ' + key + ' (Harga Rp ' + str(value) + ')')
        if pilihan in ('B', 'b'):
            print('Data buah :')
            for key, value in buah.items():
                print('- ' + key + ' (Harga Rp ' + str(value) + ')')
            print('Nama buah yang ingin dibeli : ', end='')
            nama = input()
            print('Berapa KG                   : ', end='')
            banyak = int(input())
            hasil = banyak * buah[nama]
            jumlah += hasil
            ans = input("Beli buah lainnya (y/n)? ")
            if ans in ('Y', 'y'):
                data()
            if ans in ('N', 'n'):
                print('------------------------------')
                print('Total harga :', jumlah)
                break
except ValueError:
    print('Input Invalid')
except KeyError:
    print('Invalid Key')
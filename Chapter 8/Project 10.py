buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
jumlah = 0
try:
    while True:
        print('Nama buah yang ingin dibeli : ', end='')
        nama = input()
        print('Berapa KG                   : ', end='')
        banyak = int(input())
        hasil = buah[nama] * banyak
        jumlah += hasil
        ans = input("Beli buah lainnya (y/n)? ")
        if ans in ('Y', 'y'):
            print('Nama buah yang ingin dibeli :', end='')
            nama = input()
            print('Berapa KG                   :', end='')
            banyak = int(input())
            hasil = buah[nama] * banyak
            jumlah += hasil
            ans = input("Beli buah lainnya (y/n)? ")
        if ans in ('N', 'n'):
            print('------------------------------')
            print('Total harga : ', jumlah)
            break
except ValueError:
    print('Input Invalid')
except KeyError:
    print('Invalid Key')
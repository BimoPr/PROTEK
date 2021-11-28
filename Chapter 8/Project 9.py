buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

print('Nama buah yang dibeli : ', end='')
nama = input()
try:
    if nama in buah:
        print('Berapa Kg             : ', end='')
        banyak = int(input())
        print('------------------------')
        hasil = buah[nama] * banyak
        print('Total harga           : ', hasil)
    else:
        print('Nama buah tidak terdaftar')
except ValueError:
    print("Input invalid")
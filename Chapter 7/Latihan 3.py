print('------------------------\nPROGRAM HITUNG RATA-RATA\n------------------------')
total = 0
jumlahbil = 0
while True:
    try:
        bilbul = int(input('masukkan bilangan bulat ='))
        total += bilbul
        jumlahbil += 1
        lagi = input('Lagi?(y/n): ')
        if lagi != 'y':
            if lagi == 'n':
                break
            else:
                print('data tidak valid')
                break
    except ValueError:
        print('bukan bilangan bulat')
print('\nRata-rata =',total/jumlahbil,'\n------------------------')

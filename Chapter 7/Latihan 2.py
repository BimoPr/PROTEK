direktori = input("Masukkan nama file: ")


def tambahdata():
    file.write(', ')
    file.write(input("Data yang mau ditambahkan: "))
    global tambah
    tambah = input("Mau lagi (y/n) : ")


try:
    file = open(direktori, "a")
    tambahdata()
    while True:
        if tambah == 'y':
            tambahdata()
        if tambah == 'n':
            tampilkan = input("Ingin melihat isi file (y/n): ")
            if tampilkan == 'y':
                file = open(direktori, "r")
                print(file.read())
            file.close()
            break
except FileNotFoundError:
    print("File Tidak Ada")
except ValueError:
    print('Input tidak valid')
except PermissionError:
    print("Izin tidak didapatkan")

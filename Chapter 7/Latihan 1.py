try:
    direktori = input('masukkkan direktori: ')
    print('isi file',direktori,'adalah:')
    with open(direktori) as f:
        konten = f.read()
        print(konten)
except FileNotFoundError:
    print('File tidak ditemukan')




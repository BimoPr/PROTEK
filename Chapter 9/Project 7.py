mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']


print("===================================================================================")
print('|', 'NIM'.ljust(10), '|', 'NAMA MAHASISWA'.ljust(20), '|', 'TGL LAHIR'.ljust(20),'|', 'ALAMAT'.ljust(20),'|')
print("-----------------------------------------------------------------------------------")

for data in mhs:
    split_data = data.split(':')
    space = 11
    for i in range(len(split_data)):
        if i == 2:
            tanggal = split_data[i].split('-')
            tanggal.reverse()
            print('|', '/'.join(tanggal).ljust(space), end='')
            continue
        print('|', split_data[i].ljust(space), end='')
        space= 21        
    print('|', '')

print("-----------------------------------------------------------------------------------")
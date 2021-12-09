from datetime import *
alldat = []
myfile = open('latihan3d.txt', 'w+')
retry = 'y'


def inputmember():
    memcode = input('masukkan kode member\t:')
    memnam = input('masukkan nama member\t:')
    membook = input('masukkan nama buku\t\t:')
    datee = datetime.date(datetime.now())
    retur = datee + timedelta(days=7)
    awldayt = [memcode, memnam, membook, str(datee), str(retur)]
    alldat.append(awldayt)
    global retry
    retry = input("input lagi(y/n)\t\t:")
    print()


while retry == 'y':
    inputmember()
else:
    for x in range(len(alldat)):
        myfile.write('|'.join(alldat[x])+"\n")
    myfile.close()

    #A01|Agus|Beginner Python
    #B01|Bagus|Expert Python
    #C01|Wagus|Professional Pascal|
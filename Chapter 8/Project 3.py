try:
    n = int(input('Masukkkan berapa banyaknya data mahasiswa : '))
    myList = []
    i = 0
    j = 0
    while i < n:
        nama = input("Masukkan nama mahasiswa : ")
        myList.append(nama)
        i += 1
    myList.sort()
    for i in range(len(myList)):
        print(myList[i], "(" +str(len(myList[i])), "karakter)")
except ValueError:
    print("Invalid input")
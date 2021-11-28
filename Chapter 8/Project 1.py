try:
    n = int(input("Masukkan berapa banyaknya bilangan : "))
    myList = []
    jumlah = 0
    while jumlah < n:
        bil = int(input("Masukkan bilangan anda : "))
        myList.append(bil)
        jumlah += 1
    myList.sort(reverse=True)
    print(myList)
except ValueError:
    print("Invalid input")
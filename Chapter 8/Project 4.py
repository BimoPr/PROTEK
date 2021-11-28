myList = ['bayam', 'kangkung', 'wortel', 'selada']
print("Menu:")
print("A. Tambah data sayur")
print("B. Hapus data sayur")
print("C. Tampilkan data sayur")
print(" ")

def tambah():
    tambahSayur = input("Tambahan data sayur apa nih? ")
    myList.append(tambahSayur)
def hapus():
    try:
        hapusSayur = input("Hapus data sayur yang mana nih? ")
        myList.remove(hapusSayur)
    except ValueError:
        print("Data tidak ditemukan")
def data():
    for i in range(len(myList)):
        print(myList[i])

while True:
    menu = input("Pilihan Anda (A,B,C): ")
    if menu == 'A':
        tambah()
    if menu == 'B':
        hapus()
    if menu == 'C':
        data()
        break
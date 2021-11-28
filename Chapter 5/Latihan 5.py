from random import randint
print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
AngkaRahasia = randint(0, 100)
while(True):
    tebak = int(input("Tebakan Anda: "))
    if(tebak > AngkaRahasia):
        print("Bilangan tebakan anda terlalu besar")
    elif(tebak < AngkaRahasia):
        print("Bilangan tebakan anda terlalu kecil")
    else:
        print("Yeayyy.... Bilangan tebakan anda BENAR :-)")
        break
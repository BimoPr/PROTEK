from random import randint
print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")
score = 100
AngkaRahasia = randint(0, 100)
while(True):
    if(score < 1):
        print("\nAnda sudah tidak diperbolehkan bermain karena score sudah habis")
        break
    tebak = int(input("Tebakan Anda: "))
    if(tebak > AngkaRahasia):
        print("Bilangan tebakan anda terlalu besar")
    elif(tebak < AngkaRahasia):
        print("Bilangan tebakan anda terlalu kecil")
    else:
        print("Yeayyy.... Bilangan tebakan anda BENAR :-)")
        print("\nScore Anda: ",score)
        break
    score -= 2

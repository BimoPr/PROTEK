buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def rerata():
    hasil = sum(buah.values())/len(buah)
    print('Rata-ratanya : Rp', hasil)

rerata()
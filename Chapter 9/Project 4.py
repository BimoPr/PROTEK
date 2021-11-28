import random
string = 'protek'
ulang = (int(input('Berapa Kali Perulangan? ')))
def shuffleString(x, n):
    list_ = []
    while True:
        i = ''.join(random.sample(x,len(x)))
        if i in list_:
            continue
        else:
            list_.append(i)
            n-=1
            if n==0:
                print(list_)
                break

print('randomString(', string, ulang,') -> ', end='')
shuffleString(string, ulang)
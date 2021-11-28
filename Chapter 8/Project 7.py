buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
def myfunc():
    return lambda a:a[1]
urutan = sorted(buah.items(), key=myfunc(), reverse=True)
for i in urutan:
    print(i[0])
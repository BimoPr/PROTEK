def kuadrat(x):
    hasil = []
    for i in range(len(x)):
        hasil.append(x[i]**2)
    return hasil

bil = [2, 4, 5, 6]
hasil = kuadrat(bil)
print(hasil)
myData = ['apel', 'rambutan', 'jeruk ']

def sortStringByChar(x):
    urutan = sorted(x, key=len, reverse=True)
    return  urutan

print(sortStringByChar(myData))
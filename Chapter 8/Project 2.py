myList = [4, 7, 6, 1, 5]
def dataStat(x):
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    myList2 = [a, b, c]
    return myList2
print(dataStat(myList))
#zadnie1
def podzial(a_lista,b_lista):
    res =[]
    for i in a_lista:
        if (i % 2 == 0):
            res.append(i)
    for i in b_lista:
        if(i% 2 == 1):
            res.append(i)

    return res

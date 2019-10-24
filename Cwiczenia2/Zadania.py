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

#zadanie2
def slownik(data_text):
    letters =[]
    for i in range(0,len(data_text),1):
        letters.append(data_text[i])

    dict = {'length':len(data_text), 'letters': letters,'Big_letters': data_text.upper(),
            'small_letters': data_text.lower()}
    return dict
#zadanie3
def deleter(text,letter):
    text = text.replace(letter,"")


# zadanie 4
print(dir("ciag tekstowy"))
help("ciag tekstowy".isspace())
# zadanie 5

a = "Michał Wróblewski"
print(a[::-1])

#zadanie 6
a =[1,2,3,4,5,6,7,8,9,10]
b =[]
for i in range(len(a) -1,4,-1):
    b.append(a.pop(i))
print(a)
print(b)
#zadnie7
a.extend(b)
a.insert(0,0)
c = a
a.sort()
print(a)
#zadanie8
ab= (12,"jacek")
bb = (157,"Marek")
cb = (1654,"Mariusz")
dd = ab,bb,cb
print(dd)
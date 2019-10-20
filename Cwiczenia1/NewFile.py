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
#zadanie9
slownik = dict(dd)
print(slownik)

#zadanie10
lis = [48444,221912,48444,121231,6453242,48444,996953,5346,654672,48444]
s = set(lis)
print(s)
#zadanie11
for i in range(10):
    print(i + 1)
#zadanie 12
for i in range(100,20,-5):
    print(i)

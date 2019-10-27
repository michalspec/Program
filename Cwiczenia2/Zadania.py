from Cwiczenia2 import file_manager as fm
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

#zadanie4
def convert(degrees,temperature_type):
    if(temperature_type == 'kel'):
        kel = degrees + 273.15
        return kel
    elif(temperature_type == 'faren'):
        farenh = 32 + 9 / 5 * degrees
        return farenh
    else:
        rankine = 9/5 *degrees + 273.15
        return rankine

#zadanie5
class Calculator:

    def add(number1,number2):
        return number1 + number2
    def difference(number1, number2):
        return number1 - number2
    def multiply(number1,number2):
        return number1*number2
    def divide(number1,number2):
        return number1/number2
#zadanie6
class ScienceCalculator(Calculator):
    def power(base,index):
        return pow(base,index)

#zadanie7
def reverse(text):
    return text[::-1]


#zadanie9
file = []
fm.FileManager.read_file(file)
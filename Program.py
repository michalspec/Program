a = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym." \
    " Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej" \
    " książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. " \
    "Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do " \
    "realizacji druków na komputerach osobistych, jak Aldus PageMaker"

imie = "Michał"
nazwisko = "Wróblewski"

print("W tekście jest " + str(a.count(imie[2])) + " liter " + imie[1]  + " oraz "
      +str(a.count(nazwisko[3])) +" liter "+ nazwisko[2])
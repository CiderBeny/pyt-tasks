Stan = float(input("Jaki jest twój stan początkowy konta w PLN? \t"))
Stopa = float(input("Jaka jest roczna stopa oprocentowania? \n"))*0.01
Lata = int(input("Na ile lat chcesz założyć lokatę?\n"))*12
Wynik = Stan*(1 +Stopa/12)**Lata
Wynik2 = round(Wynik,2)
print ("Twoje",Stan,"zł przez",Lata/12,"lat i oprocentowaniu",Stopa," w skali roku urośnie do",Wynik2,"zł")




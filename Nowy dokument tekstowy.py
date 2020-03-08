print("1 po angielsku: {} \n2 po angielsku: {}".format('one', 'two'))
print("Cyfra {} poprzedza {}".format(7,8))
print("Rekord świata na 100m to {} ustanowił go {}".format(9.58, 'Usain Bolt'))
print("Rekord świata na 100m to {:.2f} ustanowił go {}".format(9.5877, 'Usain Bolt'))

szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| %6.3f | %16s | %10s |" % (9.58, "Usain Bolt", "16.08.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Tyson Gay", "20.09.2009"))
print("| %6.3f | %16s | %10s |" % (9.69, "Yohan Blake", "23.09.2012"))
print("| %6.3f | %16s | %10s |" % (9.74, "Asafa Powell", "2.09.2008"))
print("-" * szer)

szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.58, "Usain Bolt", "16.08.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Tyson Gay", "20.09.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Yohan Blake", "23.09.2012"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.74, "Asafa Powell", "2.09.2008"))
print("-" * szer)

szer = 42
print("-" * szer)
print("|  Czas  |     Zawodnik     |    Data    |")
print("*" * szer)
print("| {:6.1f} | {:16s} | {:10s} |" .format(9.58, "Usain Bolt", "16.08.2009"))
print("| {:6.2f} | {:16s} | {:10s} |" .format(9.69, "Tyson Gay", "20.09.2009"))
print("| {:6.3f} | {:16s} | {:10s} |" .format(9.69, "Yohan Blake", "23.09.2012"))
print("| {:6.1f} | {:16s} | {:10s} |" .format(9.74, "Asafa Powell", "2.09.2008"))
print("-" * szer)

waluta = 'dolar'
us = 1
pln = 4.08234915
print("Aktualnie %d %s kosztuje %.2f zł" % (us, waluta, pln))
print("Aktualnie %r %r kosztuje %r zł" % (us, waluta, pln))
print("Aktualnie %r %s kosztuje %r zł" % (us, waluta, pln))

print ("{} ma {}".format("Ala", "kota"))
print ("{1} ma {0}".format("Ala", "kota"))


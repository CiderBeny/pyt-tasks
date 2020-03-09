'''#zrobic dwie plansze 10x10 z ponumerowanymi miejscami 
plansza = []
class Plansza():
 
  def __init___(self, wiersz, kolumna):
    self.x = wiersz
    self.y = kolumna
    
    
  def zwroc(self, wiersz):
    return self.x
  
  def pusta_plansza(self):
    ile_razy = 0
    plansza = []
    for i in range(10):
      x = ("|_","|_","|_","|_","|_","|_","|_","|_","|_","|_|")
      plansza.append(x)
    for linia in plansza:
      for znak in linia:
        if(ile_razy != 9):
          print(znak, end = "")
          ile_razy += 1
        else:
          print(znak, end = '\n')
          ile_razy = 0
    
  def pelna_plansza(self, kolumna):
    for litera in kolumna:
      print("|", self.wiersz[0], litera)
      
      

''' 
wiersz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kolumna = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
def plansza():
   
  ile_razy = 0
  nr_wiersza = 0
  for i in range(10):
    for litera in kolumna:
      ile_razy += 1
      if nr_wiersza != 9:
        print("|", wiersz[nr_wiersza], litera, end = " ")
      else:
        print("|", wiersz[nr_wiersza], litera, end = "")
      if ile_razy == 10:
        print('\n',"------------------------------------------------------------")
        nr_wiersza += 1
        ile_razy = 0
        
plansza()

class Gra():
  def poczatek(self):
    print("Najpierw wybierz miejsca statkow")
    statek1 = input("wpisz pola jakie ma zajac statek oddzielajac je przecinkami:")
    statek2 = input("wpisz pola jakie ma zajac statek oddzielajac je przecinkami:")
    statek3 = input("wpisz pola jakie ma zajac statek oddzielajac je przecinkami:")
    statek4 = input("wpisz pola jakie ma zajac statek oddzielajac je przecinkami:")
    statek5 = input("wpisz pola jakie ma zajac statek oddzielajac je przecinkami:")
  



    
  
  



    
    
    




  

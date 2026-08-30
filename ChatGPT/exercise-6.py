import sys

# Controllo che il valore della quantità d'acqua iniziale sia un numero, e che sia maggiore o uguale a 0   
try:
   varQtaAcqInz = float(input("Inserisci la quantità d'acqua iniziale: "))
except ValueError:
   print("Valore non valido.")
   sys.exit()

if varQtaAcqInz < 0:
   print("Valore non valido, in quanto è un numero negativo.")
   sys.exit()

# Controllo che il valore della capienza inserita sia un numero
try:
   varCapienza = float(input("Inserisci la capienza: "))
except ValueError:
   print("Valore non valido.")
   sys.exit()

# Conntrollo che il valore della capienza non sia negativo, pari a zero o minore della quantità iniziale
if varCapienza <= 0:
   print("Valore non valido, in quanto è minore o pari a zero.")
   sys.exit()   
else:
   if varCapienza >= varQtaAcqInz:
      print("Serbatoio già pieno.")
      sys.exit()       

# Controllo che il valore dei litri per ciclo sia un numero, e che sia maggiore di 0   
try:
   varLitriCiclo = float(input("Inserisci i litri per ciclo: "))
except ValueError:
   print("Valore non valido.")
   sys.exit()

if varLitriCiclo <= 0:
   print("Valore non valido, in quanto è minore o pari a zero.")
   sys.exit()           

varQtaAcqAtt = varQtaAcqInz
   
# Definisco il ciclo di lettura della temperatura della macchina, fino a quando non viene inserita la paola FINE
while varQtaAcqAtt < varCapienza:
   varQtaAcqAtt = varQtaAcqAtt + varLitriCiclo
   # Stampo la temperatura inserita, se il valore è corretto
   print("Acqua presente: ", varQtaAcqAtt)

print("Serbatoio pieno.")


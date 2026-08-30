# Librerie necessarie
import sys


# Definisco il ciclo di controllo del budget 
varBudget = 100
print("Budget iniziale: ", varBudget,"€")
while varBudget > 0:

   # Recupero l'input dell'utente
   varInpBdgt = input("Importo: ")

   # Controllo se l'utente ha richiesto l'uscita dal programma
   if varInpBdgt.strip() == 'FINE':
     print("Operazione terminata")
     print("Budget residuo: ", varBudget,"€")
     break

   # Recupero e controllo il parametro inserito, non può essere:
   # Una stringa
   # Minore o uguale a zero
   # Superiore al budget attuale
   try:
     varInpBdgt = float(varInpBdgt)
   except ValueError:
     print("Il valore inserito non risulta essere corretto.")  
     continue

   if varInpBdgt <= 0:
      print("Il valore inserito non risulta essere corretto, in quanto minore o uguale a zero.")  
      continue

   if varInpBdgt > varBudget:
      print("Budget insufficiente.")
      continue

   varBudget = round((varBudget - varInpBdgt),2)
   print("Budget residuo: ",varBudget,"€")

   if varBudget == 0:
      print("Budget esaurito.")
      break


       



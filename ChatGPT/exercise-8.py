# Librerie necessarie
import sys
import random

# Recupero il numero segreto
varSecretNumber = random.randint(1, 20)

# Definisco il ciclo di controllo del numero, con un massimo di 5 tentativi
varCnt = 0
while varCnt < 5:
   # Recupero e controllo il parametro, non può essere un carattere o fuori range
   try:
     varInputNumber = int(input('Inserisci il numero esatto: '))
   except ValueError:
     print("Il valore inserito non risulta essere un numero, ritenta.")  
     continue

   if varInputNumber < 1 or varInputNumber > 20:
      print("Il numero inserito deve essere compreso tra 1 e 20, ritenta.")
      continue

   varCnt += 1
   if varInputNumber == varSecretNumber:
     print("Hai indovinato!")
     break
   else:
     if varInputNumber < varSecretNumber:
       print("Valore troppo basso.")  
     else:
       print("Valore troppo alto.")  

   if varCnt == 5:
     print("Tentativi esauriti. Il numero era: ",varSecretNumber)        



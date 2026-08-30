# Librerie necessarie
import sys

# Funzione controllo password
def checkPassword(varPwd):
   if varPwd == 'python123':
      return True
   else:
      return False

# Definisco il ciclo di controllo della password
varCnt = 0
while varCnt < 3:
   varCnt += 1
   varInsPwd = input('Inserisci la password: ')
   # Controllo la password
   if checkPassword(varInsPwd) == True:
     print("Accesso consentito.")
     break
   else:
     print("Password errata.") 
     if varCnt == 3:
       print("Accesso bloccato.")  
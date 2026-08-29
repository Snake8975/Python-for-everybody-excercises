# Import librerie
import sys

# Reperisco e valido la temperatura iniziale della macchina, inserita dall'utente
try:
    varInpTempInz = float(input("Inserisci la temperatura iniziale, rilevata, della macchina: "))
except ValueError:
   print("Il valore inserito non risulta essere un numero.")
   sys.exit()

# Reperisco e valido la temperatura obiettivo della macchina, inserita dall'utente
try:
    varInpTempOb = float(input("Inserisci la temperatura obiettivo della macchina: "))
except ValueError:
   print("Il valore inserito non risulta essere un numero.")
   sys.exit()

# Controllo che la temperatura della macchina non sia inferiore a quella obiettivo
if varInpTempInz < varInpTempOb:
   print("La temperatura iniziale della macchina risulta essere inferiore a quella obiettivo.")
   sys.exit()

# Reperisco e valido i gradi di raffreddamento, per ciclo, inseriti dall'utente
try:
    varInpTempCiclo = float(input("Inserisci i gradi di raffreddamento, per ciclo, della macchina: "))
except ValueError:
   print("Il valore inserito non risulta essere un numero.")
   sys.exit()

# Controllo che i gradi di raffreddamento per ciclo abbiano un valore maggiore di zero
if varInpTempCiclo <= 0:
   print("I gradi di raffreddamento per ciclo devono avere un valore maggiore di zero.")
   sys.exit()

# Valorizzo la temperatura attuale della macchina con quella iniziale
varTempAtt = varInpTempInz

while varTempAtt > varInpTempOb:
   varTempAtt = varTempAtt - varInpTempCiclo
   print("La temperatura attuale della macchina è pari a: ", varTempAtt, "°")

print("Raffreddamento completato, la temperatura attuale della macchina è pari a: ", varTempAtt, "°")


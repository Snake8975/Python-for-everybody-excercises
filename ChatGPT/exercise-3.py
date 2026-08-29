# Import librerie
import sys

# Definisco le funzioni
def controlla_stato_macchina(varTemp, varPress):
      
      if varTemp > 100 or varPress > 8:
         return ("ARRESTO")  
      elif (varTemp > 80 and varTemp <= 100):
         return ("ATTENZIONE")
      elif (varPress > 6 and varPress <= 8):
         return ("ATTENZIONE")
      else:
         return ("NORMALE")


# Reperisco e valido la temperatura inserita dall'utente
try:
    varInpTemp = float(input("Inserisci la temperatura rilevata: "))
except ValueError:
   print("Il valore inserito non risulta essere un numero.")
   sys.exit()

# Controllo che la temperatura inserita sia corretta
if varInpTemp < 0 or varInpTemp > 120:
   print("Il valore inserito risulta essere un numero minore di zero o maggiore di 120.")
   sys.exit()

# Reperisco e valido la pressione inserita dall'utente
try:
    varInpPressione = float(input("Inserisci la pressione rilevata: "))
except ValueError:
   print("Il valore inserito non risulta essere un numero.")
   sys.exit()

# Controllo che la pressione inserita sia corretta
if varInpPressione < 0 or varInpPressione > 10:
   print("Il valore inserito risulta essere un numero minore di zero o maggiore di 10.")
   sys.exit()
  
# Controllo lo stato della macchina, in base alla temperatura e alla pressione rilevate
varStatMacc = controlla_stato_macchina(varInpTemp, varInpPressione)

print("Temperatura: ", varInpTemp,"°, Pressione: ", varInpPressione," bar, Stato macchina: ", varStatMacc)


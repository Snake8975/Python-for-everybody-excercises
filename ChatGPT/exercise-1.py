# Import librerie
import sys

# Reperisco le ore di sosta del veicolo e calcolo il costo totale del parcheggio
try:
    varInpOreSosta = float(input("Inserisci le ore di sosta del veicolo: "))
except ValueError:
   varInpOreSosta  = 0

# Controllo che il dato inserito sia corretto
if varInpOreSosta <= 0:
   print("Il valore inserito risulta errato.")
   sys.exit()

# Arrottondo per eccesso le ore di sosta, qualora si fosse superata l'ora (come fanno i parcheggi reali)
varOreSosta = int(varInpOreSosta)
if (varInpOreSosta - varOreSosta) > 0:  
   varOreSosta = varOreSosta + 1

# Calcolo il totale da pagare
if varOreSosta <= 2:
   varTotPagare = varOreSosta * 2.50
elif varOreSosta <=5:
   varTotPagare = 5 + ((varOreSosta - 2) * 1.8)
else:
   varTotPagare = 10.4 + ((varOreSosta - 5) * 1.2)
   if varTotPagare > 15:
      varTotPagare = 15

print("Il costo del parcheggio è pari a:", varTotPagare,"€")
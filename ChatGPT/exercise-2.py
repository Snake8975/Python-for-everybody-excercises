# Import librerie
import sys

# Definisco le funzioni
def calcola_prezzo_spedizione(varPeso, varCoeff):
      if varPeso <=2:
         return (5 * varCoeff)
      elif varPeso <=5:
         return (8 * varCoeff) 
      elif varPeso <=10:
         return (12 * varCoeff) 
      else:
         return ((12 + (varPeso - 10) * 1.5) * varCoeff) 


# Reperisco e valido il peso del pacco
try:
    varInpPesoPacco = float(input("Inserisci il peso del pacco: "))
except ValueError:
   print("Il valore inserito non risulta essere un numero.")
   sys.exit()

# Controllo che il dato inserito sia corretto
if varInpPesoPacco <= 0:
   print("Il valore inserito risulta essere un numero minore o pari a zero.")
   sys.exit()

# Reperisco il dato relativo spedizione express e lo normalizzo.
varInpSpExpress = input("E' una spedizione Express (SI/NO)? ")
varInpSpExpress = varInpSpExpress.strip()


if varInpSpExpress.upper() == 'SI':
   varCoeffSped = 1.3
elif varInpSpExpress.upper() == 'NO': 
   varCoeffSped = 1
else:
   print("Ti è stato detto di inserire un valore che fosse SI o NO; qualsiasi altro valore invalida l'operazione, " \
   "pertanto dovrai ricominciare da capo, MONA!")
   sys.exit()
  
# Calcolo il valore della spedizione e lo riporto all'utente
varTotSped = calcola_prezzo_spedizione(varInpPesoPacco, varCoeffSped)

print("Il costo della spedizione è pari a:", round(varTotSped,2),"€")


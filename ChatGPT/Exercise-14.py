import random

# Funzione di conteggio dei caratteri da 0 a 9:
def countChar(parmStrig):
    varCount = 0
    varrArray = ['0','1','2','3','4','5','6','7','8','9']
    for letter in parmStrig:

        if letter in varrArray:
          varCount = varCount + 1

    return  varCount      

# Recupero la stringa principale
while True:
    varString = input("Inserisci un codice identificativo di almeno 6 caratteri: ")
    if len(varString.strip()) <= 5:
        print("Attenzione: il numero di caratteri inserito è insuffuciente.")
        continue

    varString = varString.strip()
    break    

# Stampo i primi due caratteri:
print("Primi due caratteri: ", varString[0:2]) 

# Stampo gli ultimi due caratteri:
varLenStr = len(varString)
print("Ultimi due caratteri: ", varString[(varLenStr-2):varLenStr]) 

# Stampo la parte centrale della stringa:
print("Parte centrale: ", varString[1:(varLenStr-1)])

# Controllo presenza carattere '-':
if "-" in varString:
    print("Contiene '-': SI")
else:
    print("Contiene '-': NO")    

# Stampo il numero di volte che compare una cifra tra 0 e 9:
print("Numero di cifre: ", countChar(varString))

# Stampo il codice modificato:
varStringX = 'X'+varString[1:(varLenStr+1)]
print("Codice modificato: ",varStringX)
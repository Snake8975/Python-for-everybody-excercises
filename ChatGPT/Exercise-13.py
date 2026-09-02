# Funzione di conteggio della lettera A:
def countLetterA(parmStrig):
    varCount = 0
    for letter in parmStrig:
        if letter == 'a':
          varCount = varCount + 1

    return  varCount      

# Funzione di controllo presenza lettera E:
def presenceLetterE(parmStrig):
    if ('e' in parmStrig):
        return 'SI'
    else:
        return 'NO'

# Recupero la stringa principale
while True:
    varString = input("Inserisci una stringa: ")
    if len(varString.strip()) == 0:
        print("E' obbligatorio inserire un valore.")
        continue

    break    

varLenStr = len(varString)

# Stampo i caratteri
print("Primo carattere: ",varString[0])
print("Ultimo carattere: ",varString[(varLenStr-1)])
print("Primi 3 caratteri: ",varString[0:3])
print("Ultimi 3 caratteri: ",varString[(varLenStr-3):(varLenStr)])
print("Senza il primo e l'ultimo: ",varString[1:(varLenStr-1)])
print("Numero di 'a': ",countLetterA(varString))
print("contiene 'e': ",presenceLetterE(varString))
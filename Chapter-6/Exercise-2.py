# Funzione di conteggio dei caratteri:
def countChar(parmStrig, parmChar):
    varCount = 0
    for letter in parmStrig:
        if letter == parmChar:
          varCount = varCount + 1

    return  varCount      

# Recupero la stringa principale
while True:
    varString = input("Inserisci una stringa: ")
    if len(varString.strip()) == 0:
        print("E' obbligatorio inserire un valore.")

    break    


# Recupero la stringa da controllare
while True:
    varStringChk = input("Inserisci i caratteri da ricercare: ")
    if len(varStringChk.strip()) < 0 or len(varStringChk.strip()) > 1:
        print("Attenzione, devi inserire un solo carattere.")

    break    

# Stampo il conteggio dei caratteri
print("Il carattere è apparso ",countChar(varString, varStringChk)," volte.")
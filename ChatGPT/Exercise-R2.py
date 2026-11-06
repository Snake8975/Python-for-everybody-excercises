# Inizializzo le variabili  
varSomma = 0
varMax = None
varMin = None
varCount = 0

# Ciclo di inserimento dei numeri
while True:
    
    # Controllo input
    varNum = input("Inserisci un numero: ")
    if varNum.strip().lower() == 'done':
        break
    try:
        varNum=float(varNum)
    except ValueError:
        print("Attenzione: Il valore inserito non è un numero.")
        continue

    # Conteggio, somma, minimo e massimo
    varCount += 1
    varSomma = varSomma + varNum
    if varMax is None or varNum > varMax:
        varMax = varNum
    
    if varMin is None or varNum < varMin:
        varMin = varNum    

  
if varCount == 0:
    print("Non è stato inserito alcun numero")
else:    
    # Stampa risultati 
    print(f"Sono stati inseriti {varCount} numeri.")
    print(f"La somma dei numeri inseriti è pari a {varSomma}.")
    print(f"Il valore massimo inserito è: {varMax}.")
    print(f"Il valore minimo inserito è: {varMin}.")
    print(f"La media dei numeri è pari a: {varSomma/varCount}.")
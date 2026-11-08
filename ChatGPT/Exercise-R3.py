# Funzioni 
# Somma 
def fzSomma(a, b):
    return a + b

# Sottrazione
def fzSottrazione(a, b):
    return a - b

# Moltiplicazione
def fzMoltiplicazione(a, b):
    return a * b

# Divisione
def fzDivisione(a, b):
    return a / b    

# Ciclo principale
while True:

    # Ciclo di inserimento numeri e operatori
    # Numero 1
    while True:
        
        # Controllo input
        varNum1 = input("Inserisci il primo numero: ")
        try:
            varNum1=float(varNum1)
        except ValueError:
            print("Attenzione: Il valore inserito non è un numero.")
            continue
        break

    # Numero 2
    while True:
        
        # Controllo input
        varNum2 = input("Inserisci il secondo numero: ")
        try:
            varNum2=float(varNum2)
        except ValueError:
            print("Attenzione: Il valore inserito non è un numero.")
            continue
        break

    # Operatore
    while True:
        
        # Controllo input
        varOperatore = input("Inserisci un operatore valido, tra + (somma), - (sottrazione), * (moltiplicazione),  / (divisione): ")
        if varOperatore.strip() in ('+', '-', '*', '/'):
            varOperatore = varOperatore.strip()
            break
        else:
            print("Attenzione: Il valore inserito non è un operatore.")
            continue     
    

    # Risultato dell'operazione
    match varOperatore:
        case '+':
            print(f'La somma è pari a: {fzSomma(varNum1, varNum2)}')
        case '-':
            print(f'La differenza è pari a: {fzSottrazione(varNum1, varNum2)}')
        case '*':
            print(f'Il prodotto è pari a: {fzMoltiplicazione(varNum1, varNum2)}')
        case '/':
            if varNum2 == 0:
                print("Errore: Divisione per zero.")
            else: 
                print(f'Il quoziente è pari a: {fzDivisione(varNum1, varNum2)}')

    while True:
        varMsgExit = ''
        varContinue = input("Vuoi eseguire un'altra operazione? ")
        if varContinue.strip().lower() == 'no':
            varMsgExit = 'Programma terminato.'
            break
        elif varContinue.strip().lower() == 'si':
            break
        else:
            print('La risposta può essere solo si/no')
            continue  

    if varMsgExit=='':
        continue
    else:
        break

print(varMsgExit)  


  

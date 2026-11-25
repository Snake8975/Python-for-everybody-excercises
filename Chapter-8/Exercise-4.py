# Ciclo inserimento dei parametri
tList=[]

while True:
    varInpNumber = input("Inserisci un numero (done per uscire): ")
    if varInpNumber.strip().lower()=='done':
        break

    # Controllo numero
    try:
        tList.append(int(varInpNumber))
    except ValueError:
        print("Errore: inserisci un numero o done per uscire.")

# Controlli finali e stampa input
if len(tList)<0:
    print("Non è stato inserito alcun elemento.")
elif len(tList)==1:
       print(f"Il valore inserito è pari a: {tList[0]}") 
else:
    print(f"Il valore massimo inserito è pari a: {max(tList)}")
    print(f"Il valore minimo inserito è pari a: {min(tList)}")


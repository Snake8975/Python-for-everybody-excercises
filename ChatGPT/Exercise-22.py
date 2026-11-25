# Ciclo inserimento dei parametri
tList=[]

while True:
    varInpNumber = input("Inserisci la temperatura rilevata (done per uscire): ")
    if varInpNumber.strip().lower()=='done':
        break

    # Controllo numero
    try:
        tList.append(float(varInpNumber))
    except ValueError:
        print("Errore: inserisci una temperatura valida o done per uscire.")

# Controlli finali e stampa
if len(tList)<=0:
    print("Non è stata inserita alcuna temperatura.")
else:
    print("Le temperature inserite sono pari a: ") 
    for n in tList: print(f"{n}°C")
    print(f"Il valore massimo inserito è pari a: {max(tList)}°C")
    print(f"Il valore minimo inserito è pari a: {min(tList)}°C")
    print(f"La media delle temperature è la seguente: {round(sum(tList)/len(tList), 2)}°C")
    print(f"Il numero delle temperature che superano i 25 gradi è pari a: {sum(1 for n in tList if n > 25)}")


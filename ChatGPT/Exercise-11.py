# Dichiaro le variabili
varIncasso = 0
varIncassoTotale = 0
varIncassoMax = None
varIncassoMaxStr = None
varIncassoMin = None
varIncassoMinStr = None
varIncassoOver500 = 0
varIdx = 0
varDayNum = 0

# Ciclo for dei giorni della settimana:
for varIdx in range(7):
    varDayNum += 1
    varAskIncasso = "Inserisci l'incasso della giornata numero "+str(varDayNum)+": "
    # Ciclo while per l'inserimento dell'incasso giornaliero
    while True:

        # Controllo la variabile dell'incasso del giorno
        try:
            varIncasso = float(input(varAskIncasso))
        except ValueError:
            print("Il valore inserito non è valido.")
            continue

        if varIncasso < 0:
            print("Il valore inserito non può essere un numero minore di zero.")
            continue

        # Esco dopo aver recuperato il valore corretto del giorno 
        break    

    # Incasso più basso della settimana
    if varIncassoMin is None or varIncassoMin > varIncasso:
        varIncassoMin = varIncasso
        varIncassoMinStr = "Giorno " + str(varDayNum) + " - "  + str(varIncasso) + "€"

    # Incasso più alto della settimana
    if varIncassoMax is None or varIncassoMax < varIncasso:
        varIncassoMax = varIncasso
        varIncassoMaxStr = "Giorno " + str(varDayNum) + " - " + str(varIncasso) + "€"

    # Numero giorni con incasso superiore ai 500€
    if varIncasso > 500:
       varIncassoOver500 += 1 

    # Totale temperature
    varIncassoTotale = varIncassoTotale + varIncasso   

# Stampa resoconto
print("Totale incasso settimanale: ", varIncassoTotale)
print("Incasso medio settimanale: ", (varIncassoTotale/7))
print("Incasso massimo: ", varIncassoMaxStr)
print("Incasso minimo: ", varIncassoMinStr)
print("L'incasso giornaliero superiore ai 500€ è stato superato " ,varIncassoOver500 ," volte")
# Dichiaro le variabili
varNumTemp = 0
varTempMax = None
varTempMin = None
varNumTempOver30 = 0
varTotTemp = 0
varIdx = 0

# Ciclo while per l'inserimento del numero di temperature da rilevare
while True:

    # Controllo la variabile iteratore
    try:
        varNumTemp = int(input("Quante volte vorresti rilevare la temperatura? "))
    except ValueError:
        print("Il valore inserito non è valido.")
        continue

    if varNumTemp <= 0:
        print("Il valore inserito non può essere un numero minore o uguale a zero.")
        continue

    # Esco dopo aver recuperato il valore corretto per l'iteratore    
    break    

while varIdx < varNumTemp:
    # Controllo che sia stao inserito un numero
    try:
        varTemp = float(input("Qual'è la temperatura rilevata? "))
    except ValueError:
        print("Il valore inserito non è valido, in quanto non è un numero.")
        continue

    varIdx += 1
    # Temperatura minima e massima
    if varTempMin is None or varTempMin > varTemp:
        varTempMin = varTemp

    if varTempMax is None or varTempMax < varTemp:
        varTempMax = varTemp

    # Temperatura sopra i 30 gradi.
    if varTemp > 30:
       varNumTempOver30 += 1 

    # Totale temperature
    varTotTemp = varTotTemp + varTemp   

print("La temperatura minima rilevata è stata: ", varTempMin)
print("La temperatura massima rilevata è stata: ", varTempMax)
print("La somma di tutte le temperature è pari a: ", varTotTemp)
try:
    print("La media artimetica è pari a: ", (varTotTemp/varIdx))
except ZeroDivisionError:    
    print("La media artimetica risulta un numero indefinito, in quanto il dividendo è pari a 0")
print("La temperatura superiore ai 30 gradi è stata rilevata per " ,varNumTempOver30 ," volte")
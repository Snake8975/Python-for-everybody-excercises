import sys

while True:
    varStringOrd = input("Inserisci la stringa con struttura ORD-ANNO-SEDE-NUMERO:") 
    varStringOrd = varStringOrd.strip()

    # Controllo la lunghezza della stringa
    if len(varStringOrd) != 17:
        print("Codice non valido")
        continue

    varOrd = varStringOrd[0:3].upper()
    varAnno = varStringOrd[4:8]
    varSede = varStringOrd[9:11].upper()
    varNumero = varStringOrd[12:17]

    # Controllo la presenza e la corretta posizione dei caratteri "-"
    if varStringOrd.count('-') != 3:
        print("Codice non valido")
        continue       

    if varStringOrd[3] != '-' or varStringOrd[8] != '-' or varStringOrd[11] != '-':
        print("Codice non valido")
        continue       


    # Controllo che lunghezza e valori della stringa sia corretti
    if  len(varOrd.strip()) != 3  or len(varAnno.strip()) != 4 or  len(varSede.strip()) != 2 or  len(varNumero.strip()) != 5:
        print("Codice non valido")
        continue

    # Controllo se le prime tre lettere siano ORD
    if varOrd != 'ORD': 
        print("Codice non valido")
        continue

    # Stampo l'output
    print(f'Ordine {varNumero} - sede {varSede} - anno  {varAnno}')
    break


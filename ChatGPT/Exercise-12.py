# Inizializzo le variabili
varStringa = None
varCharChk = None
varPrima_posizione = None
varNumVolte = 0
varLenStringa = 0
varPosArray = 0

# Recupero i parametri di ingresso 
# Testo da processare
while True:
    varStringa = input("Inserisci la stringa che vuoi processare: ")
    if len(varStringa.strip()) == 0:
        print("Inserisci almeno una parola. Ritenta")
        continue

    break

# Carattere da ricercare
while True:
    varCharChk = input("Inserisci il carattere che vuoi ricercare: ")
    if len(varCharChk.strip()) == 0 or len(varCharChk.strip()) > 1:
        print("Inserisci un carattere. Ritenta")
        continue

    varCharChk = varCharChk.strip()    
    break

for varSingleChar in varStringa:
    if varSingleChar == varCharChk:
        varNumVolte += 1
        if varPrima_posizione is None:
            varPrima_posizione = varPosArray

    varPosArray += 1

if varNumVolte > 0:
    print("Occorrenze: ", varNumVolte)
    print("Prima posizione: ", varPrima_posizione)
else:
    print("Il carattere richiesto, non è presente nella stringa.")    







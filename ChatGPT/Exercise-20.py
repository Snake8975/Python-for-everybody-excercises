# Inizializzazione delle variabili
varConta = 0
varSomma = 0

# Ciclo di recupero e controllo della directory
while True:
    varFilenName = input("Inserisci il nome del file: ")
    varPathFile = "D:/repository/Python/Python-for-everybody-excercises/ChatGPT/" + varFilenName.strip() + ".txt"

    # Controllo esistenza directory
    try:
        fhandle = open(varPathFile, "r")
    except:
        print("File non trovato o percorso errato. Controlla il nome del file e riprova.")
        continue
    break


# Elaborazione righe del file
for lines in fhandle:
    if lines.startswith('X-DSPAM-Confidence:'): 
        varConta += 1
        varExtFloat = float(lines[lines.find(':')+1:].strip())
        varSomma = varSomma + varExtFloat


# Stampa dei risultati
print(f"Sono stati trovati {varConta} valori all'interno del file di log")
print(f"Il totale dei valori nel file di log è pari a: {varSomma}")
print(f"La media è pari a: {varSomma/varConta}")


while True:
    varStringName = input("Inserisci la stringa con struttura NOME-COGNOME-ANNO:") 
    varStringName = varStringName.strip()

    # Controllo la presenza e la corretta posizione dei caratteri "=" e ";"
    try:
        varNome, varCognome, varAnno = varStringName.split(';')
    except ValueError:
        print("La struttura deve contenere esattamente tre campi.")
        continue

    varNome = varNome.strip()
    varCognome = varCognome.strip()
    varAnno = varAnno.strip()

    # Controllo la posizione dei parametri
    if not varNome.startswith("NOME=") or not varCognome.startswith("COGNOME=") or not varAnno.startswith("ANNO="):
        print("L'ordine dei parametri è errato, dev'essere così: NOME, COGNOME, ANNO")
        continue       

    varNome = varNome[5:].strip()
    varCognome = varCognome[8:].strip()
    varAnno = varAnno[5:].strip()    

    # Controllo che le variabili siano presenti e valorizzate
    if len(varNome) < 1: 
        print("Il campo NOME è vuoto.")
        continue 
    else:
        if len(varCognome) < 1: 
           print("Il campo COGNOME è vuoto.")
           continue 
        else:
            if len(varAnno) != 4: 
               print("Il campo ANNO è vuoto o non è nel formato YYYY.")
               continue 

    # Stampo l'output
    print(f'{varCognome} {varNome} - anno di nascita: {varAnno}')
    print(f'Iniziali: {varNome[0].upper()}{varCognome[0].upper()}')
    break


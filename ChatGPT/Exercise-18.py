import sys

while True:
    varStringName = input("Inserisci la stringa con struttura NOME-COGNOME-ANNO:") 
    varStringName = varStringName.strip()

    # Controllo la presenza e la corretta posizione dei caratteri "=" e ";"
    if varStringName.count('=') != 3 or varStringName.count(';') != 2:
        print("Record non valido.")
        continue    

    # Controllo la presenza dei parametri
    if varStringName.find('NOME=') is False: 
        print("Record non valido.")
        continue 
    else:
        if varStringName.find('COGNOME=') is False: 
           print("Record non valido.")
           continue 
        else:
            if varStringName.find('ANNO=') is False: 
               print("Record non valido.")
               continue 

    # Controllo la posizione dei parametri
    if (varStringName.find('NOME=') > varStringName.find('COGNOME=')) or (varStringName.find('NOME=') > varStringName.find('ANNO=')) or (varStringName.find('COGNOME=') > varStringName.find('ANNO=')): 
        print("Record non valido.")
        continue       

    # Recupero le variabili
    varNome = varStringName[varStringName.find('NOME='), varStringName.find(';')]
    varCognome = varStringName[varStringName.find('COGNOME='), varStringName.find(';', (varStringName.find('COGNOME=')+1),  (varStringName.find('ANNO=')-1))]
    varAnno = varStringName[varStringName.find('ANNO='), -1]
    varNome = varNome.strip()
    varCognome = varCognome.strip()
    varAnno = varAnno.strip()

    # Controllo che le variabili siano presenti e valorizzate
    if len(varNome) < 1: 
        print("Record non valido.")
        continue 
    else:
        if len(varCognome) < 1: 
           print("Record non valido.")
           continue 
        else:
            if len(varCognome) != 4: 
               print("Record non valido.")
               continue 

    # Stampo l'output
    print(f'{varCognome} {varNome} - anno di nascita: {varAnno}')
    break


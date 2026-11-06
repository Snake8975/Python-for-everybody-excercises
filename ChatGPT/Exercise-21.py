import sys

while True:

    # Controllo del file
    varFile = input("Inserisci il nome del file:") 
    varPathFile = f"D:/{varFile.strip()}.txt"

    try:    
        fhandle = open(varPathFile)
    except:
        print("Errore: file non trovato o path non valido")
        continue

    # Inizializzazione e conteggi
    varCountINFO = 0   
    varCountWARN = 0  
    varCountERROR = 0   
    varCountStsD = 0  
    varCountStsQ = 0      
    varCountFrom = 0   
    for lines in fhandle:
        if 'INFO' in lines: varCountINFO +=1    
        if 'WARN' in lines: varCountWARN +=1    
        if 'ERROR' in lines: varCountERROR +=1
        if 'Status: delivered' in lines: varCountStsD +=1    
        if 'Status: quarantined' in lines: varCountStsQ +=1       
        if lines.startswith('From:'): varCountFrom +=1

    break       

# Stampa risultati
print(f"INFO: {varCountINFO}")
print(f"WARN: {varCountWARN}")
print(f"ERROR: {varCountERROR}")
print(f"Messaggi consegnati: {varCountStsD}")
print(f"Messaggi in quarantena: {varCountStsQ}")
print(f"Messaggi totali analizzati: {varCountFrom}")
# Funzioni
def funzioneControlloAperturaFile(varNomeFile):
    try:
        varFile = open(varNomeFile, 'r')
        print(f'File {varNomeFile} aperto correttamente.')
        return varFile
    except FileNotFoundError:
        print(f'Errore: il file {varNomeFile} non esiste.')
        return None
    except IOError:
        print(f'Errore: impossibile aprire il file {varNomeFile}.')
        return None
    

# Ciclo principale
while True:
    varNomeFile = input('Inserisci il percorso del file di log (o "exit" per uscire): ')
    if varNomeFile.lower() == 'exit':
        break
    varFile = funzioneControlloAperturaFile(varNomeFile)
    if varFile is None:
        continue

    varCount = 0
    varCountINFO = 0
    varCountWARN = 0
    varCountERROR = 0
    varCountOperazioniLente = 0
    varTotalTempoEsecuzione = 0.0
    varTempoMin = None
    varTempoMax = None

    for varRiga in varFile:
        varCount += 1
        varListLog = varRiga.split('|') 

        # Ricavo il livello di log
        varLivelloLog = varListLog[1].strip()
        match varLivelloLog:
            case "INFO":
                varCountINFO += 1
            case "WARN":
                varCountWARN += 1
            case "ERROR":
                varCountERROR += 1
            
        # Ricavo il tempo di esecuzione
        varTempoEsecuzione = varListLog[4].strip().split('=')[1]
        varTempoEsecuzione = float(varTempoEsecuzione)

        # Somma dei tempi di esecuzione
        varTotalTempoEsecuzione = varTotalTempoEsecuzione + varTempoEsecuzione

        # Massimo
        if varTempoMax is None or varTempoMax < varTempoEsecuzione:
            varTempoMax = varTempoEsecuzione
            varUtenteMax = varListLog[2].strip().split('=')[1]
            varAzioneMax = varListLog[3].strip().split('=')[1]

        # Minimo
        if varTempoMin is None or varTempoMin > varTempoEsecuzione:
            varTempoMin = varTempoEsecuzione
            varUtenteMin = varListLog[2].strip().split('=')[1]
            varAzioneMin = varListLog[3].strip().split('=')[1]

        # Numero operazioni lente
        if varTempoEsecuzione > 0.5:
            varCountOperazioniLente += 1

    # Stampa elaborazione
    if varCount > 0:

        print('========== LOG ANALYZER ==========')
        print('\n')
        print(f'Eventi analizzati: {varCount}')
        print('\n')
        print(f'INFO: {varCountINFO}')
        print(f'WARN: {varCountWARN}')
        print(f'ERROR: {varCountERROR}')
        print('\n')
        print(f'Operazioni lente: {varCountOperazioniLente}')
        print('\n')
        print(f'Tempo totale: {varTotalTempoEsecuzione} secondi')
        print(f'Tempo medio: {varTotalTempoEsecuzione/varCount} secondi')
        print('\n')
        print('--- OPERAZIONE PIÙ LENTA ---')
        print(f'Utente: {varUtenteMax}')
        print(f'Azione: {varAzioneMax}')
        print(f'Tempo: {varTempoMax}')    
        print('\n')
        print('--- OPERAZIONE PIÙ VELOCE ---')
        print(f'Utente: {varUtenteMin}')
        print(f'Azione: {varAzioneMin}')
        print(f'Tempo: {varTempoMin}')    
        print('\n')
        print('==================================')
    else:
        print('Attenzione: Nessuna riga presente nel file')

    # Uscita dal ciclo principale
    varFile.close()
    break

print('\n')
print('Programma terminato.')





  
